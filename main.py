import sys

from PyQt6.QtWidgets import QApplication

from MVC import controller
from MVC.gui import GUI
from MVC.model import Model
from MVC import stylesheet


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(stylesheet.get_stylesheet())
    model = Model()
    gui = GUI()
    gui.show()
    controller = controller.Controller(model=model, view=gui)
    sys.exit(app.exec())
