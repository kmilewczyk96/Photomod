from PyQt6.QtWidgets import (
    QGraphicsOpacityEffect,
    QWidget
)


def addOpacityEffect(element: QWidget, initialToggle=True):
    opacity = QGraphicsOpacityEffect()
    opacity.setOpacity(0.2)
    element.setGraphicsEffect(opacity)
    opacity.setEnabled(initialToggle)
