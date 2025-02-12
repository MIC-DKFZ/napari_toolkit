from typing import Callable, Optional

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QHBoxLayout, QLabel, QLayout, QSlider, QWidget

from napari_toolkit.utils.utils import connect_widget
from napari_toolkit.widgets.sliders.double_slider import QDoubleSlider


class _QLabeledSlider(QWidget):
    """A base class for sliders with an associated label displaying the current value.

    This class provides common methods for integer and floating-point sliders with labels.
    """

    def setMinimum(self, value: int) -> None:
        """Sets the minimum value of the slider.

        Args:
            value (int): The minimum value to set.
        """
        self.slider.setMinimum(value)

    def setMaximum(self, value: int) -> None:
        """Sets the maximum value of the slider.

        Args:
            value (int): The maximum value to set.
        """
        self.slider.setMaximum(value)

    def setValue(self, value: int) -> None:
        """Sets the current value of the slider.

        Args:
            value (int): The new slider value.
        """
        self.slider.setValue(value)

    def value(self) -> int:
        """Retrieves the current slider value.

        Returns:
            int: The current slider value.
        """
        return self.slider.value()

    def setTickInterval(self, value: int) -> None:
        """Sets the tick interval for the slider.

        Args:
            value (int): The tick interval.
        """
        self.slider.setTickInterval(value)

    def update_label(self, value: int) -> None:
        """Updates the label to reflect the current slider value.

        Args:
            value (int): The updated slider value.
        """
        self.label.setText(f"{self.value()}")


class QLabeledSlider(_QLabeledSlider):
    """A labeled slider for displaying integer values.

    This widget consists of a `QSlider` and a `QLabel` that updates dynamically
    to reflect the slider's current value.
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initializes the QLabeledSlider widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
        """
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

    def setMaximum(self, value: int) -> None:
        """Sets the maximum value of the slider and adjusts label width accordingly.

        Args:
            value (int): The maximum value to set.
        """
        super().setMaximum(value)
        self.label.setFixedWidth(10 + len(str(value)) * 10)


class QLabeledDoubleSlider(_QLabeledSlider):
    """A labeled slider for displaying floating-point values.

    This widget consists of a `QDoubleSlider` and a `QLabel` that updates dynamically
    to reflect the slider's current value.

    Attributes:
        max_digits (int): Maximum number of digits for label formatting.
    """

    def __init__(self, parent: Optional[QWidget] = None, digits: int = 1) -> None:
        """Initializes the QLabeledDoubleSlider widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            digits (int, optional): Number of decimal places for displayed values. Defaults to 1.
        """
        super().__init__(parent)
        layout = QHBoxLayout()
        self.max_digits = 2
        self.slider = QDoubleSlider(digits=digits)
        self.slider.setOrientation(Qt.Horizontal)
        self.label = QLabel()

        layout.addWidget(self.slider, stretch=10)
        layout.addWidget(self.label, stretch=1)

        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.update_label)

    def setMaximum(self, value):
        """Sets the maximum value of the slider and adjusts label width accordingly.

        Args:
            value (float): The maximum value to set.
        """
        super().setMaximum(value)
        self.label.setFixedWidth(10 + (len(str(int(value))) + self.max_digits) * 10)


def setup_labeledslider(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    tick_size: Optional[int] = None,
    default: Optional[int] = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QLabeledSlider, configure it, and add it to a layout.

    This function creates a `QLabeledSlider` widget, sets its range, tick size,
    and default value if provided. It connects an optional callback function to
    the slider's `sliderReleased` signal and adds it to the specified layout.

    Args:
        layout (QLayout): The layout to which the QLabeledSlider will be added.
        minimum (Optional[int], optional): The minimum value of the slider. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the slider. Defaults to None.
        tick_size (Optional[int], optional): The interval between slider ticks. Defaults to None.
        default (Optional[int], optional): The initial value of the slider. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the slider is released. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QLabelSlider widget added to the layout.
    """
    _widget = QLabeledSlider()

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
        widget_event=_widget.slider.sliderReleased,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_labeleddoubleslider(
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
    """Create a QLabeledDoubleSlider, configure it, and add it to a layout.

    This function creates a `QLabeledDoubleSlider` widget, sets its range, tick size,
    and default value if provided. It connects an optional callback function to
    the slider's `sliderReleased` signal and adds it to the specified layout.

    Args:
        layout (QLayout): The layout to which the QLabeledDoubleSlider will be added.
        digits (int, optional): The number of decimal places for the float slider. Defaults to 2.
        minimum (Optional[int], optional): The minimum value of the slider. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the slider. Defaults to None.
        tick_size (Optional[int], optional): The interval between slider ticks. Defaults to None.
        default (Optional[int], optional): The initial value of the slider. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the slider is released. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QFloatLabelSlider widget added to the layout.
    """
    _widget = QLabeledDoubleSlider(digits=digits)

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
        widget_event=_widget.slider.sliderReleased,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
