from napari_plugin_engine import napari_hook_implementation
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton, QVBoxLayout, QWidget


class QToggleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)  # Makes it toggleable
        self.clicked.connect(self.toggle_button)

    def toggle_button(self):
        if self.isChecked():
            self.setStyleSheet("background-color:  rgb(0,100, 167);")
        else:
            self.setStyleSheet("")
