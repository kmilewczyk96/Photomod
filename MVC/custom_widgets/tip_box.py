from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLineEdit,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QToolButton,
    QVBoxLayout,
    QWidget
)


class TipBox(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 38)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        self.info = QLabel()  # Demo
        # info = QLabel()
        self.info.setFixedHeight(18)

        self.details = QLabel()  # Demo
        # details = QLabel()
        self.details.setFixedHeight(18)

        layout.addWidget(self.info)
        layout.addWidget(self.details)
        self.setLayout(layout)

    def clear(self):
        self.info.setText('')
        self.details.setText('')
