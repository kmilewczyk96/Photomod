from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QRadioButton


class SelectButton(QRadioButton):
    """
    Customized QRadioButton, purpose of this class is to unify operation buttons style.
    IMPORTANT!: cssIdName should be lowercase section name so the automatic styling could be applied.
    """
    def __init__(self, cssIdName: str, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(92, 38)
        self.setEnabled(False)  # Set as disabled by default.
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty('class', f'selectBtn {cssIdName.split("-")[0]}Btn')
        self.setObjectName(cssIdName)
