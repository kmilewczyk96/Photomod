from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QRadioButton,
    QGraphicsDropShadowEffect,
    QGraphicsBlurEffect,
    QGraphicsOpacityEffect
)


class SelectButton(QRadioButton):
    def __init__(self, cssIdName: str):
        super().__init__()
        self.setFixedSize(92, 38)
        self.setEnabled(False)  # Set as disabled by default.
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty('class', f'selectBtn {cssIdName.split("-")[0]}Btn')
        self.setObjectName(cssIdName)
