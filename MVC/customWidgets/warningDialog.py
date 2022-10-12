from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import (
    QDialog,
    QGraphicsDropShadowEffect,
    QVBoxLayout,
    QLabel
)


from .warningList import WarningList


class WarningDialog(QDialog):
    def __init__(self, parent, warningList):
        super().__init__(parent=parent)
        self.warningList = warningList
        self._setWindowPersonalization()
        self.setWindowIcon(QIcon('../../resources/icons/warning-icon.png'))
        self.setWindowTitle('Operacja nie może zostać wykonana!')
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self._createContent()

    def _setWindowPersonalization(self):
        self.setProperty('class', 'warningDialog')
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, False)

    def show(self) -> None:
        self.exec()

    def _createContent(self):
        labelTip = QLabel('Zmień nazwę poniższych plików lub wybierz inny folder docelowy:')
        self.layout().addWidget(labelTip)
        if self.warningList:
            self.layout().addWidget(self.warningList)
