import numpy as np
from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSlider,
    QWidget,
)

from napari_toolkit.widgets.float_slider import QFloatSlider


class QSliderEdit(QWidget):
    index_changed = Signal()

    def __init__(self, parent=None, min_value=0, max_value=100, start_value=0):
        super().__init__(parent)

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = start_value
        self.init_ui()
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(self.min_value)
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
        if self.min_value <= value <= self.max_value:
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.slider.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self):
        self.set_value(self.current_value + 1)

    def decrement_value(self):
        self.set_value(self.current_value - 1)


class QFloatSliderEdit(QWidget):
    index_changed = Signal()

    def __init__(self, parent=None, min_value=0, max_value=100, start_value=0, digits=1):
        super().__init__(parent)
        self.digits = digits
        self.digit_factor = 10**digits

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = start_value
        self.init_ui()
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self):
        self.slider = QFloatSlider(self, digits=self.digits)
        self.slider.setOrientation(Qt.Horizontal)

        self.slider.setMinimum(self.min_value)
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
            value = self.slider.value()
            self.line_edit.setText(str(value))
        except ValueError:
            pass

    def update_progress(self):
        try:
            value = float(self.line_edit.text())
            self.set_value(value)
        except ValueError:
            pass

    def set_value(self, value):
        if self.min_value <= value <= self.max_value:
            value = np.round(value, self.digits)
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.slider.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self):
        self.set_value(self.current_value + 10 ** (-self.digits))

    def decrement_value(self):
        self.set_value(self.current_value - 10 ** (-self.digits))
