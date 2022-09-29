import re

from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import (
    QLineEdit,
    QFrame,
    QHBoxLayout,
    QPushButton
)


class CustomLineEdit(QFrame):
    def __init__(self, buttonText: str):
        super().__init__()
        self.setProperty('class', 'renameDiv')
        self.setFixedSize(206, 38)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.lineEdit = QLineEdit('IMG_')
        self.lineEdit.setProperty('class', 'renameInput')
        self.lineEdit.setFixedHeight(36)
        self.lineEdit.setMaxLength(32)
        pathValidator = QRegularExpressionValidator()
        regex = QRegularExpression()
        regex.setPattern(r'[^\\/:*?"<>|]*')
        pathValidator.setRegularExpression(regex)
        self.lineEdit.setValidator(pathValidator)

        self.button = QPushButton(buttonText)
        self.button.setFixedHeight(36)
        self.button.setContentsMargins(0, 0, 0, 0)
        self.button.setProperty('class', 'renameBtn')
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)
