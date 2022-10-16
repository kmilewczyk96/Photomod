from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QGraphicsOpacityEffect,
    QHBoxLayout,
    QPushButton
)

from .progressBarDiv import ProgressBarDiv


class ExecuteDiv(QFrame):
    """Special div that stores submitBtn and progressBarDiv created separately for each process."""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 24, 0, 24)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)
        self.setFixedHeight(86)
        self._createBtn()
        self.layout.addWidget(self.submitBtn)
        self._createOpacity()

    def setEnabled(self, a0: bool) -> None:
        super().setEnabled(a0)
        self.graphicsEffect().setEnabled(True if not a0 else False)

    def switchToExecution(self):
        """Disables and hides submitBtn and creates new progress bar div."""
        self.submitBtn.setEnabled(False)
        self.submitBtn.hide()
        self._createProgressBar()
        self.layout.addWidget(self.progressBarDiv)

    def switchToStandBy(self):
        """Removes progress bar div from layout and destroys it. Enables submitBtn back."""
        self.layout.removeWidget(self.progressBarDiv)
        del self.progressBarDiv
        self.submitBtn.show()
        self.submitBtn.setEnabled(True)

    def _createBtn(self):
        self.submitBtn = QPushButton('Wykonaj')
        self.submitBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submitBtn.setProperty('class', 'submitBtn')
        self.submitBtn.setFixedSize(206, 38)

    def _createOpacity(self):
        """Sets default graphic effect for execution div, disabled by default."""
        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(0.2)
        self.setGraphicsEffect(opacity)
        self.setGraphicsEffect(opacity)

    def _createProgressBar(self):
        self.progressBarDiv = ProgressBarDiv(parent=self)

