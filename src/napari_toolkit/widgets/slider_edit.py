from napari_plugin_engine import napari_hook_implementation
from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QSlider,
)


class QSliderEdit(QWidget):
    index_changed = Signal()

    def __init__(self, parent=None, max_value=100, start_value=0):
        super().__init__(parent)

        self.max_value = max_value
        self.current_value = start_value
        self.init_ui()
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.max_value)
        self.slider.setValue(self.current_value)
        self.slider.valueChanged.connect(self.update_edit)
        self.slider.sliderReleased.connect(self.update_progress)
        self.slider.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.current_value))
        self.line_edit.returnPressed.connect(self.update_progress)
        self.line_edit.setContentsMargins(0, 0, 0, 0)

        self.next_button = QPushButton("+", self)
        self.next_button.clicked.connect(self.increment_value)
        self.next_button.setContentsMargins(0, 0, 0, 0)

        self.prev_button = QPushButton("-", self)
        self.prev_button.clicked.connect(self.decrement_value)
        self.prev_button.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.slider, stretch=10)
        layout.addWidget(self.prev_button, stretch=2)
        layout.addWidget(self.line_edit, stretch=3)
        layout.addWidget(self.next_button, stretch=2)

        self.setLayout(layout)

    def update_edit(self):
        try:
            value = int(self.slider.value())
            self.line_edit.setText(str(value))
        except ValueError:
            pass

    def update_progress(self):
        try:
            value = int(self.line_edit.text())
            self.set_value(value)
        except ValueError:
            pass

    def set_value(self, value):
        if 0 <= value <= self.max_value:
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.slider.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self):
        self.set_value(self.current_value + 1)

    def decrement_value(self):
        self.set_value(self.current_value - 1)
