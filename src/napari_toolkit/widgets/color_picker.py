from qtpy.QtGui import QColor
from qtpy.QtWidgets import QColorDialog, QPushButton


class QColorPicker(QPushButton):
    def __init__(self, initial_color=(255, 255, 255), size=30):
        super().__init__()

        self.setFixedSize(size, size)  # Make the button square
        self.color = QColor.fromRgb(*initial_color)
        self.update_button_color()
        self.clicked.connect(self.pick_color)

    def pick_color(self):
        color = QColorDialog.getColor(self.color)
        if color.isValid():
            self.color = color
            self.update_button_color()

    def update_button_color(self):
        """Update the button background to the selected color."""
        self.setStyleSheet(f"background-color: {self.color.name()}; border: 1px solid black;")

    def get_color(self):
        """Return the selected color as a hex string."""
        return self.color.getRgb()[0:3]
