import sys
from functools import partial

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import (
    QFileDialog,
    QLineEdit,
    QButtonGroup
)

from .gui import GUI
from .image_operations import ImageWorker
from .model import Model
from .utils.shorten_path import getShortenedPath
from .customWidgets.warningDialog import WarningDialog
from .customWidgets.warningList import WarningList


class Controller:
    def __init__(self, model: Model, view: GUI):
        super().__init__()
        self._model = model
        self._view = view
        self._connectSignalsAndSlots()

    def _connectSignalsAndSlots(self):
        # File buttons:
        self._view.targetDirButton.clicked.connect(self._launchFolderSelect)
        self._view.chooseFilesButton.clicked.connect(self._launchFilesSelect)

        # Toggle buttons:
        renameToggleButton = self._view.renameDiv.toggleButton
        rotateToggleButton = self._view.rotateDiv.toggleButton
        resolutionToggleButton = self._view.resolutionDiv.toggleButton

        renameToggleButton.clicked.connect(partial(self._toggleRename, renameToggleButton))
        rotateToggleButton.clicked.connect(partial(self._toggleRotate, rotateToggleButton))
        resolutionToggleButton.clicked.connect(partial(self._toggleResolution, resolutionToggleButton))

        # Button groups:
        rotateGroup = self._view.rotateGroup
        self._view.rotateGroup.buttonClicked.connect(partial(self._selectRotateIndex, rotateGroup))
        resolutionGroup = self._view.resolutionGroup
        self._view.resolutionGroup.buttonClicked.connect(partial(self._selectResolutionIndex, resolutionGroup))

        # Check indexes button:
        checkIndexesButton = self._view.checkIndexesButton
        checkIndexesButton.clicked.connect(self._checkIndexes)

        # Inputs:
        self._view.renameInput.lineEdit.textEdited.connect(partial(self._updatePrefix, self._view.renameInput.lineEdit))

        # Execute button:
        self._view.submitBtn.clicked.connect(self._executeOperations)
        self._view.continueBtn.clicked.connect(self._switchToExecution)

    @staticmethod
    def _toggleEffects(widgets: list, toggle: bool):
        for widget in widgets:
            widget.setEnabled(toggle)
            try:
                opacity = widget.graphicsEffect()
                opacity.setEnabled(False if toggle else True)
            except AttributeError:
                print("Element doesn't have graphic effects.")

    def _toggleRename(self, button):
        toggle = button.isChecked()
        self._model.rename = toggle
        widgets = button.parent().components
        self._toggleEffects(widgets=widgets, toggle=toggle)

        if toggle:
            self._view.renameTipBox.setHidden(False)
        else:
            self._view.renameTipBox.setHidden(True)

    def _toggleRotate(self, button):
        toggle = button.isChecked()
        self._model.rotate = toggle
        widgets = button.parent().components
        self._toggleEffects(widgets=widgets, toggle=toggle)

    def _toggleResolution(self, button):
        toggle = button.isChecked()
        self._model.resolution = toggle
        widgets = button.parent().components
        self._toggleEffects(widgets=widgets, toggle=toggle)

    def _selectRotateIndex(self, group: QButtonGroup):
        self._model.rotateIndex = group.checkedId()

    def _selectResolutionIndex(self, group: QButtonGroup):
        self._model.resolutionIndex = group.checkedId()

    def _launchFolderSelect(self):
        """Launches QFileDialog allowing User to pick target directory."""
        path = QFileDialog.getExistingDirectory(directory='/home/Karol', options=QFileDialog.Option.ShowDirsOnly)
        if path:
            # Styling:
            limit = 40
            strPath = path if len(path) <= 40 else getShortenedPath(path=path, limit=limit)
            self._view.targetDirButton.setText(strPath.replace('/', '\\') if sys.platform == 'win32' else strPath)
            self._view.targetDirButton.pseudoCheck()
            self._view.targetDirButton.checked = True

            # Operation:
            self._model.targetPath = path
            self._checkFilesSelected()

    def _launchFilesSelect(self):
        """Launches QFileDialog allowing User to pick images he wants to work with."""
        files, _ = QFileDialog.getOpenFileNames(directory='/home/Karol/Pictures', filter='jpg(*.jpg *.JPG)')
        filesCount = len(files)
        if filesCount:
            # Styling:
            self._view.chooseFilesButton.setText(f'Wybrano {filesCount} plików.')
            self._view.chooseFilesButton.pseudoCheck()
            self._view.chooseFilesButton.checked = True

            # Operation:
            self._model.files = files
            # self._view.progressDialog.setMaximum(filesCount)
            self._checkFilesSelected()

    def _updatePrefix(self, lineEdit: QLineEdit):
        self._view.renameTipBox.clear()
        self._model.prefix = lineEdit.text()
        self._model.nextIndex = None

    def _executeOperations(self) -> None:
        """
        Creates QThread and ImageWorker instances responsible for running all image operations.
        """
        self._model.runOperations()

        # Create Worker object and move it to the new QThread:
        self.thread = QThread()
        self.worker = ImageWorker(model=self._model)
        self.worker.moveToThread(self.thread)
        abort = self._view.abortBtn.clicked.connect(self.thread.requestInterruption)

        self.thread.started.connect(partial(self._switchToProgressBar, len(self._model.files)))
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(partial(self._view.abortBtn.disconnect, abort))
        self.thread.finished.connect(self._switchToConfirmation)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.progress.connect(self._updateProgress)
        self.worker.filenamesError.connect(self._createWarningDialog)

        self.thread.start()

    def _createWarningDialog(self, warningListItems: list):
        warningList = WarningList(warningListItems=warningListItems)
        self.warningDialog = WarningDialog(parent=self._view, warningList=warningList)
        self.warningDialog.errorBtn.clicked.connect(self.warningDialog.hide)
        self.warningDialog.errorBtn.clicked.connect(self._switchToExecution)
        self.warningDialog.show()

    def _updateProgress(self, index: int):
        self._view.progressBar.setValue(index)

    def _checkIndexes(self):
        nextFreeIndex = self._model.checkExistingPrefixes()
        self._model.nextIndex = nextFreeIndex

        self._view.renameTipBox.info.setText('Pierwszy wolny index:')
        self._view.renameTipBox.details.setText(
            f'{self._model.prefix}{str(self._model.nextIndex + 1).zfill(5)}.jpg'
        )

    def _checkFilesSelected(self):
        """If all files have been selected, enable access to operations div."""
        valuesRequired = (
            self._model.targetPath,
            self._model.files
        )
        for value in valuesRequired:
            if not value:
                return False

        # Set enabled and remove opacity effect:
        self._view.operationsDiv.graphicsEffect().setEnabled(False)
        self._view.operationsDiv.setEnabled(True)
        self._view.submitBtn.graphicsEffect().setEnabled(False)
        self._view.submitBtn.setEnabled(True)

    def _switchToProgressBar(self, maxValue: int):
        self._view.submitBtn.hide()
        self._view.progressDiv.barFilled(bool_=False)
        self._view.progressBar.setMaximum(maxValue)
        self._view.progressBar.setValue(0)
        self._view.progressDiv.show()

    def _switchToConfirmation(self):
        self._view.progressDiv.barFilled(bool_=True)

    def _switchToExecution(self):
        self._view.progressBar.reset()
        self._view.progressDiv.barFilled(bool_=False)
        self._view.progressDiv.hide()
        self._view.submitBtn.setEnabled(True)
        self._view.submitBtn.show()

    @staticmethod
    def __signalTest():
        print('Signal!')
