from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFrame,
    QGraphicsOpacityEffect,
    QLabel,
    QVBoxLayout
)


class SectionDiv(QFrame):
    """Container for section contents, taking section name as the only parameter."""
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
        self._createOpacity()

    def setEnabled(self, a0: bool) -> None:
        """Enable graphics effect on disabling."""
        super().setEnabled(a0)
        self.graphicsEffect().setEnabled(True if not a0 else False)

    def _createOpacity(self):
        """Sets default graphic effect for section div, disabled by default."""
        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(0.2)
        self.setGraphicsEffect(opacity)
        self.graphicsEffect().setEnabled(False)
