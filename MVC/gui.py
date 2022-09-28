import os
import sys

from PyQt6.QtCore import (
    Qt,
    QPoint
)
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
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
from .custom_widgets.custom_line_edit import CustomLineEdit
from .custom_widgets.div import Div
from .custom_widgets.file_push_button import FilePushButton
from .custom_widgets.operation_div import OperationDiv
from .custom_widgets.select_button import SelectButton
from .custom_widgets.tip_box import TipBox
from .utils.graphic_effects_handler import addOpacityEffect


class GUI(QMainWindow):
    marginS = 8
    marginM = 12
    marginL = 16
    marginXL = 24

    def __init__(self):
        super(GUI, self).__init__(parent=None)
        self.setWindowTitle('Photomod')
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(12)
        self.setContentsMargins(12, 12, 12, 4)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central = QWidget(self)
        central.setLayout(self.mainLayout)
        self.setCentralWidget(central)
        self._createPickFolder()
        self._createOperations()
        self._createButtons()

    def _createPickFolder(self):
        div = Div('Pliki:')
        # Section items:
        form = QFormLayout()
        form.setVerticalSpacing(self.marginS)
        form.setHorizontalSpacing(self.marginL)
        self.targetDirButton = FilePushButton('Wybierz')
        self.chooseFilesButton = FilePushButton('Wybierz')
        form.addRow('Folder docelowy:', self.targetDirButton)
        form.addRow('Pliki do edycji:', self.chooseFilesButton)
        div.layout.addLayout(form, stretch=False)
        self.mainLayout.addWidget(div)

    def _createOperations(self):
        div = Div('Operacje:')

        self.renameDiv = self._createRenameDiv()
        div.layout.addWidget(self.renameDiv)
        div.layout.addSpacing(self.marginXL)

        self.rotateDiv = self._createRotateDiv()
        div.layout.addWidget(self.rotateDiv)
        div.layout.addSpacing(self.marginXL)

        self.resolutionDiv = self._createResolutionDiv()
        div.layout.addWidget(self.resolutionDiv)

        self.mainLayout.addWidget(div)
        self.toggleableItems = [self.renameDiv, self.rotateDiv, self.resolutionDiv]
        # x = QGraphicsOpacityEffect()
        # x.setOpacity(0.5)
        # div.setGraphicsEffect(x)

    def _createRenameDiv(self):
        renameDiv = OperationDiv('Zmień nazwę:')

        self.renameToggleButton = renameDiv.toggleButton
        self.renameInput = CustomLineEdit(buttonText='Sprawdź')
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

    def _createButtons(self):
        div = QHBoxLayout()
        div.setContentsMargins(0, 50, 0, 20)
        self.submitBtn = QPushButton('Wykonaj')
        self.submitBtn.setProperty('class', 'btn-submit')
        self.submitBtn.setStyleSheet('background-color: #087f5b; color: #f8f9fa;')
        self.submitBtn.setFixedSize(200, 40)
        self.submitBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        div.addWidget(self.submitBtn, stretch=False, alignment=Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addLayout(div)
