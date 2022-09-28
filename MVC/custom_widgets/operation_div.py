from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QWidget
)

from .toggle_slider import ToggleSlider


class OperationDiv(QFrame):
    def __init__(self, toggleLabel: str):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = ToggleSlider(label=toggleLabel)
        vDiv = QVBoxLayout()
        vDiv.setContentsMargins(0, 0, 0, 0)
        vDiv.addWidget(self.toggleButton)
        vDiv.addSpacing(8)

        self.components = []
        self.componentsDiv = QHBoxLayout()
        self.componentsDiv.setContentsMargins(12, 0, 12, 0)
        self.componentsDiv.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.componentsDiv.setSpacing(24)
        vDiv.addLayout(self.componentsDiv)
        self.setLayout(vDiv)

    def addWidget(self, widget: QWidget):
        self.components.append(widget)
        self.componentsDiv.addWidget(widget)
