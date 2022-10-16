from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QProgressBar,
    QPushButton
)


class ProgressBarDiv(QFrame):
    def __init__(self, parent, width=436, height=27):
        super().__init__(parent=parent)
        self.setObjectName('progressDiv')
        self.setFixedSize(width, height)
        buttonsWidth = width // 5
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.bar = QProgressBar(parent=self)
        self.bar.setFixedHeight(height)
        self.bar.setObjectName('progressBar')
        layout.addWidget(self.bar)

        self.abortBtn = QPushButton('Przerwij', parent=self)
        self.abortBtn.setFixedSize(buttonsWidth, height)
        self.abortBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.abortBtn.setProperty('class', 'progressBtn')
        self.abortBtn.setObjectName('abortBtn')
        layout.addWidget(self.abortBtn)

        self.continueBtn = QPushButton('Kontynuuj', parent=self)
        self.continueBtn.setFixedSize(buttonsWidth, height)
        self.continueBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.continueBtn.setProperty('class', 'progressBtn')
        self.continueBtn.setObjectName('continueBtn')
        self.continueBtn.setEnabled(False)
        self.continueBtn.hide()
        layout.addWidget(self.continueBtn)

        self.setLayout(layout)

    def barFilled(self, bool_: bool):
        if bool_:
            self.abortBtn.setEnabled(False)
            self.abortBtn.hide()
            self.continueBtn.setEnabled(True)
            self.continueBtn.show()
        else:
            self.continueBtn.setEnabled(False)
            self.continueBtn.hide()
            self.abortBtn.setEnabled(True)
            self.abortBtn.show()
