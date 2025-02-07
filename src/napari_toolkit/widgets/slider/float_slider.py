import numpy as np
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QSlider


class QFloatSlider(QSlider):
    """Custom QSlider that handles floating point values."""

    floatValueChanged = Signal(float)  # Signal for float values

    def __init__(self, parent=None, digits=1):
        super().__init__(parent)
        self.digits = digits
        self.digit_factor = 10**digits

    def setTickInterval(self, value):
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setTickInterval(value)

    def setMaximum(self, value):
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setMaximum(value)

    def setMinimum(self, value):
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setMinimum(value)

    def setValue(self, value):
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setValue(value)

    def value(self):
        value = super().value()
        return value / self.digit_factor

    # def emit_float_value(self, int_value):
    #     float_value = self.min_value + int_value * self.step
    #     self.floatValueChanged.emit(float_value)
    #
    # def setFloatValue(self, float_value):
    #     int_value = int((float_value - self.min_value) / self.step)
    #     self.setValue(int_value)
    #
    # def getFloatValue(self):
    #     return self.min_value + self.value() * self.step
