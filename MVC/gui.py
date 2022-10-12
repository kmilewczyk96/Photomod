import os
import sys
import time

from PyQt6.QtCore import (
    Qt,
    QPoint
)
from PyQt6.QtGui import QColor, QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QProgressDialog,
    QDialog,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QProgressBar,
    QSlider,
    QSpinBox,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QComboBox,
    QSizePolicy,
    QGraphicsDropShadowEffect,
    QGraphicsOpacityEffect
)
from .customWidgets.lineEditDiv import LineEditDiv
from .customWidgets.div import Div
from .customWidgets.warningDialog import WarningDialog
from .customWidgets.warningList import WarningList
from .customWidgets.filesButton import FilesPushButton
from .customWidgets.operation_div import OperationDiv
from .customWidgets.progress_div import ProgressDiv
from .customWidgets.selectButton import SelectButton
from .customWidgets.tipBox import TipBox
from .utils.graphic_effects_handler import addOpacityEffect


class GUI(QMainWindow):
    """
    This class is responsible for creating main layout of the app.
    Some widgets are imported from 'customWidgets' module.
    """
    marginS = 8
    marginM = 12
    marginL = 16
    marginXL = 24

    def __init__(self):
        super(GUI, self).__init__(parent=None)
        self.setWindowTitle('Photomod')
        self.setWindowIcon(QIcon('../resources/icons/window-icon.png'))
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(12)
        self.setContentsMargins(12, 12, 12, 4)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central = QWidget(self)
        central.setLayout(self.mainLayout)
        self.setCentralWidget(central)
        self._createPickFolder()
        self._createOperations()
        self._createExecutionDiv()

    def _createPickFolder(self):
        """
        Creates container with Folder and File choosing buttons.
        """
        self.filesDiv = Div('Pliki:')
        # Section items:
        form = QFormLayout()
        form.setVerticalSpacing(self.marginS)
        form.setHorizontalSpacing(self.marginL)
        self.targetDirButton = FilesPushButton('Wybierz')
        self.chooseFilesButton = FilesPushButton('Wybierz')
        form.addRow('Folder docelowy:', self.targetDirButton)
        form.addRow('Pliki do edycji:', self.chooseFilesButton)
        self.filesDiv.layout.addLayout(form, stretch=False)
        self.mainLayout.addWidget(self.filesDiv)

    def _createOperations(self):
        """
        Creates container with Available operations.
        Disabled by default!
         """
        self.operationsDiv = Div('Operacje:')
        self.operationsDiv.setEnabled(False)
        addOpacityEffect(element=self.operationsDiv)

        operationGroup = QButtonGroup(parent=self.operationsDiv)
        operationGroup.setExclusive(False)
        operationGroupDivs = []
        self.renameDiv = self._createRenameDiv()
        self.operationsDiv.layout.addWidget(self.renameDiv)
        self.operationsDiv.layout.addSpacing(self.marginXL)
        operationGroupDivs.append(self.renameDiv)

        self.rotateDiv = self._createRotateDiv()
        self.operationsDiv.layout.addWidget(self.rotateDiv)
        self.operationsDiv.layout.addSpacing(self.marginXL)
        operationGroupDivs.append(self.rotateDiv)

        self.resolutionDiv = self._createResolutionDiv()
        self.operationsDiv.layout.addWidget(self.resolutionDiv)
        self.operationsDiv.layout.addSpacing(self.marginXL)
        operationGroupDivs.append(self.resolutionDiv)

        self.mainLayout.addWidget(self.operationsDiv)
        for id_, div in enumerate(operationGroupDivs):
            operationGroup.addButton(div.toggleButton, id=id_)

    def _createRenameDiv(self):
        """
        Creates and returns container storing Rename operation interface.
        """
        renameDiv = OperationDiv('Zmień nazwę:')

        self.renameToggleButton = renameDiv.toggleButton
        self.renameInput = LineEditDiv(buttonText='Sprawdź')
        self.renameInput.setEnabled(False)
        self.checkIndexesButton = self.renameInput.button
        self.renameTipBox = TipBox()
        self.renameTipBox.setHidden(True)

        widgets = [self.renameInput, self.renameTipBox]

        for widget in widgets:
            renameDiv.addWidget(widget)
            addOpacityEffect(element=widget)

        return renameDiv

    def _createRotateDiv(self):
        """
        Creates and returns container storing Rotate operation interface.
        """
        rotateDiv = OperationDiv('Obróć obraz:')

        self.rotateGroup = QButtonGroup(parent=rotateDiv)
        self.rotateGroup.setExclusive(True)
        rotateLeft90 = SelectButton(cssIdName='rotate-left')
        rotate180 = SelectButton(cssIdName='rotate-180')
        rotateRight90 = SelectButton(cssIdName='rotate-right')

        widgets = [rotateLeft90, rotate180, rotateRight90]
        widgets[0].setChecked(True)

        for id_, widget in enumerate(widgets):
            self.rotateGroup.addButton(widget, id=id_)  # Add button to the group
            rotateDiv.addWidget(widget)  # Add button to container
            addOpacityEffect(element=widget)

        return rotateDiv

    def _createResolutionDiv(self):
        """
        Creates and returns container storing Change Resolution operation interface.
        """
        resolutionDiv = OperationDiv('Zmień rozdzielczość:')

        self.resolutionGroup = QButtonGroup(parent=resolutionDiv)
        self.resolutionGroup.setExclusive(True)
        resolution_720p = SelectButton(cssIdName='resolution-720p')
        resolution_1080p = SelectButton(cssIdName='resolution-1080p')
        resolution_1440p = SelectButton(cssIdName='resolution-1440p')
        resolution_4k = SelectButton(cssIdName='resolution-4k')

        widgets = [resolution_720p, resolution_1080p, resolution_1440p, resolution_4k]
        widgets[0].setChecked(True)

        for id_, widget in enumerate(widgets):
            self.resolutionGroup.addButton(widget, id=id_)
            resolutionDiv.addWidget(widget)
            addOpacityEffect(element=widget)

        return resolutionDiv

    def _createExecutionDiv(self):
        frame = QFrame()
        div = QHBoxLayout()
        frame.setLayout(div)
        frame.setFixedHeight(86)
        frame.layout().setAlignment(Qt.AlignmentFlag.AlignVCenter)
        div.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        div.setContentsMargins(0, 24, 0, 24)

        self.submitBtn = QPushButton('Wykonaj')
        self.submitBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submitBtn.setProperty('class', 'submitBtn')
        self.submitBtn.setFixedSize(206, 38)
        frame.layout().addWidget(self.submitBtn)

        self.progressDiv = ProgressDiv(parent=self, abortText='Przerwij', continueText='Kontynuuj', height=26)
        self.progressBar = self.progressDiv.bar
        self.continueBtn = self.progressDiv.continueBtn
        self.abortBtn = self.progressDiv.abortBtn
        frame.layout().addWidget(self.progressDiv)

        self.mainLayout.addWidget(frame)
        addOpacityEffect(element=self.submitBtn, level=0.15)
        self.submitBtn.setEnabled(False)

