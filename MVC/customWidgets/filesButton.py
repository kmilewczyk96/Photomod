from PyQt6.QtCore import (
    Qt
)

from PyQt6.QtWidgets import (
    QPushButton
)


class FilesPushButton(QPushButton):
    """
    Customized QPushButton simulating QRadio button 'Checked' state.
    Its purpose is to be checked once and never change the state after.
    """
    def __init__(self, label: str):
        super().__init__()
        self.setFixedHeight(26)
        self.setText(label)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty('class', 'fileBtn')
        self._setInitialStyle()
        self.checked = False

    def pseudoCheck(self):
        """Create effect of button being checked/enabled."""
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