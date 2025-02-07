from qtpy.QtCore import Qt
from qtpy.QtWidgets import QHBoxLayout, QLabel, QSlider, QWidget

from napari_toolkit.widgets.slider.float_slider import QFloatSlider


class _QLabelSlider(QWidget):

    def setMinimum(self, value):
        self.slider.setMinimum(value)

    def setMaximum(self, value):
        self.slider.setMaximum(value)

    def setValue(self, value):
        self.slider.setValue(value)

    def value(self):
        return self.slider.value()

    def setTickInterval(self, value):
        self.slider.setTickInterval(value)

    def update_label(self, value):
        self.label.setText(f"{self.value()}")


class QLabelSlider(_QLabelSlider):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.max_digits = 2
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.label = QLabel()

        layout.addWidget(self.slider, stretch=10)
        layout.addWidget(self.label, stretch=1)

        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.update_label)

    def setMaximum(self, value):
        super().setMaximum(value)
        self.label.setFixedWidth(10 + len(str(value)) * 10)


class QFloatLabelSlider(_QLabelSlider):
    def __init__(self, parent=None, digits=1):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.max_digits = 2
        self.slider = QFloatSlider(digits=digits)
        self.slider.setOrientation(Qt.Horizontal)
        self.label = QLabel()

        layout.addWidget(self.slider, stretch=10)
        layout.addWidget(self.label, stretch=1)

        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.update_label)

    def setMaximum(self, value):
        super().setMaximum(value)
        self.label.setFixedWidth(10 + (len(str(int(value))) + self.max_digits) * 10)
