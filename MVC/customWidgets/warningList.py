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
        self.warningListItems = warningListItems
        mainLayout = QVBoxLayout()
        self._prepareScrollArea()
        mainLayout.addWidget(self.scrollArea)
        self.setMinimumWidth(300)
        self.setMaximumHeight(150)
        self.setLayout(mainLayout)
        self._populate()

    def _populate(self):
        self.scrollLayout = QVBoxLayout(self.scrollAreaMainWidget)
        for item in self.warningListItems:
            item = QLabel(item)
            item.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.scrollLayout.addWidget(item)
        self.scrollLayout.addStretch()

    def _prepareScrollArea(self):
        self.scrollArea = QScrollArea()
        self.scrollBar = QScrollBar()
        self.scrollBar.setProperty('class', 'warningScrollBar')
        self.scrollBar.setMinimumHeight(15)
        self.scrollArea.setVerticalScrollBar(self.scrollBar)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaMainWidget = QWidget()
        self.scrollAreaMainWidget.setProperty('class', 'warningDialogScrollArea')
        self.scrollArea.setWidget(self.scrollAreaMainWidget)
