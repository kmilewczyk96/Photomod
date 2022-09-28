from PyQt6.QtCore import (
    Qt,
    QPoint
)
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QComboBox,
    QSizePolicy,
    QGraphicsDropShadowEffect,
    QGraphicsOpacityEffect
)


class FilePushButton(QPushButton):
    def __init__(self, label: str):
        super().__init__()
        self.setFixedHeight(26)
        self.setText(label)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty('class', 'fileBtn')
        self._setInitialStyle()
        self.checked = False

    def pseudoCheck(self):
        """Create effect of button being checked."""
        if not self.checked:
            self.setStyleSheet(
                """
                .fileBtn {
                    color: #087f5b;
                    background-color: #63e6be;
                    border: 2px solid #087f5b;
                    border-radius: 5;
                    padding: 0 12;
                }
                .fileBtn:hover {
                    color: #087f5b;
                    background-color: #38d9a9;
                }
                """
            )

    def _setInitialStyle(self):
        self.setStyleSheet(
            """
            .fileBtn {
                color: #495057;
                background-color: #dee2e6;
                border: 1px solid #343a40;
                border-radius: 5;
            }
            .fileBtn:hover {
                color: #212529;
                background-color: #adb5bd;
            }
            """
        )