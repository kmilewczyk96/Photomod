from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QScrollArea,
    QScrollBar,
    QWidget
)


class WarningList(QWidget):
    def __init__(self, warningListItems: list):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.warningListItems = warningListItems
        mainLayout = QVBoxLayout()
        self._prepareScrollArea()
        mainLayout.addWidget(self.scrollArea)
        self.setMaximumHeight(250)
        self.setLayout(mainLayout)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self._populate()

    def _populate(self):
        self.scrollLayout = QVBoxLayout(self.scrollAreaMainWidget)
        for item in self.warningListItems:
            item = QLabel(item)
            item.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.scrollLayout.addWidget(item)

    def _prepareScrollArea(self):
        self.scrollArea = QScrollArea()
        self.scrollArea.setProperty('class', 'warningList')
        self.scrollArea.setFrameStyle(QFrame.Shape.NoFrame)
        self.scrollBar = QScrollBar()
        self.scrollBar.setProperty('class', 'warningScrollBar')
        self.scrollBar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.scrollArea.setVerticalScrollBar(self.scrollBar)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaMainWidget = QWidget()
        self.scrollAreaMainWidget.setProperty('class', 'warningDialogScrollArea')
        self.scrollArea.setWidget(self.scrollAreaMainWidget)
