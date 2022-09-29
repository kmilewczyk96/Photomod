from PyQt6.QtWidgets import (
    QGraphicsOpacityEffect,
    QWidget
)


def addOpacityEffect(element: QWidget, level=0.2, initialToggle=True):
    opacity = QGraphicsOpacityEffect()
    opacity.setOpacity(level)
    element.setGraphicsEffect(opacity)
    opacity.setEnabled(initialToggle)
