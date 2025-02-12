from typing import Callable, Optional

import numpy as np
from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import QLayout, QSlider, QWidget

from napari_toolkit.utils.utils import connect_widget


class QDoubleSlider(QSlider):
    """A custom QSlider that supports floating-point values.

    This widget extends `QSlider` to handle floating-point values by internally
    scaling them using a specified number of decimal digits.

    Attributes:
        floatValueChanged (Signal): A signal that emits a float value when the slider changes.
        digits (int): The number of decimal places to retain.
        digit_factor (int): The factor used for internal integer scaling.
    """

    floatValueChanged = Signal(float)  # Signal for float values

    def __init__(self, parent: Optional[QSlider] = None, digits: int = 1) -> None:
        """Initializes the QDoubleSlider.

        Args:
            parent (Optional[QSlider], optional): The parent widget. Defaults to None.
            digits (int, optional): The number of decimal places for floating-point values. Defaults to 1.
        """
        super().__init__(parent)
        self.digits = digits
        self.digit_factor = 10**digits

    def setTickInterval(self, value: float) -> None:
        """Sets the tick interval for the slider.

        Args:
            value (float): The desired tick interval.
        """
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setTickInterval(value)

    def setMaximum(self, value: float) -> None:
        """Sets the maximum value for the slider.

        Args:
            value (float): The maximum float value.
        """
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setMaximum(value)

    def setMinimum(self, value: float) -> None:
        """Sets the minimum value for the slider.

        Args:
            value (float): The minimum float value.
        """
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setMinimum(value)

    def setValue(self, value: float) -> None:
        """Sets the current value of the slider.

        Args:
            value (float): The float value to set.
        """
        value = int(np.round(value, self.digits) * self.digit_factor)
        super().setValue(value)

    def value(self) -> float:
        """Retrieves the current value of the slider as a float.

        Returns:
            float: The current slider value converted back to float.
        """
        value = super().value()
        return value / self.digit_factor


def setup_doubleslider(
    layout: QLayout,
    digits: int = 2,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
    tick_size: Optional[int] = None,
    default: Optional[float] = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QDoubleSlider, configure it, and add it to a layout.

    This function creates a `QDoubleSlider` widget, sets its precision, range,
    tick size, and default value if provided. It connects an optional callback
    function to the slider's `sliderReleased` signal and adds it to the specified layout.

    Args:
        layout (QLayout): The layout to which the QDoubleSlider will be added.
        digits (int, optional): The number of decimal places for the float slider. Defaults to 2.
        minimum (Optional[float], optional): The minimum value of the slider. Defaults to None.
        maximum (Optional[float], optional): The maximum value of the slider. Defaults to None.
        tick_size (Optional[int], optional): The interval between slider ticks. Defaults to None.
        default (Optional[float], optional): The initial value of the slider. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the slider is released. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QDoubleSlider widget added to the layout.
    """
    _widget = QDoubleSlider(digits=digits)
    _widget.setOrientation(Qt.Horizontal)

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default is not None:
        _widget.setValue(default)
    if tick_size is not None:
        _widget.setTickInterval(tick_size)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.sliderReleased,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
