from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QDialog,
    QGraphicsDropShadowEffect
)


class ErrorDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self._setWindowPersonalization()
        self.setFixedWidth(400)
        self.setFixedHeight(250)
        self.hide()

    def _setWindowPersonalization(self):
        self.setProperty('class', 'section')
        self.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint, False)

    def show(self) -> None:
        self.exec()
