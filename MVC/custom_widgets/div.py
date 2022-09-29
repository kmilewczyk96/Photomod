from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)


class Div(QFrame):
    def __init__(self, sectionName: str):
        super().__init__()
        self.setProperty('class', 'section')
        self.setContentsMargins(12, 4, 12, 4)
        self.layout = QVBoxLayout()

        sectionNameLabel = QLabel(sectionName.upper())
        labelFont = sectionNameLabel.font()
        labelFont.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 1.5)
        labelFont.setBold(True)
        sectionNameLabel.setFont(labelFont)
        self.layout.addWidget(sectionNameLabel)
        self.layout.addSpacing(24)
        self.setLayout(self.layout)
