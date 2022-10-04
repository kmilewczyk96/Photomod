from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QCheckBox
)


class ToggleSlider(QCheckBox):
    """
    Custom QCheckBox.
    """
    def __init__(self, label):
        super().__init__(label)
        self.setProperty('class', 'toggle-slider')
        self.setCursor(Qt.CursorShape.PointingHandCursor)
