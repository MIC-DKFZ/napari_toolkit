from typing import Callable, Optional

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLayout, QSlider, QWidget

from napari_toolkit.setup.utils import connect_widget
from napari_toolkit.widgets.slider.edit_slider import QEditFloatSlider, QEditSlider
from napari_toolkit.widgets.slider.float_slider import QFloatSlider
from napari_toolkit.widgets.slider.label_slider import QFloatLabelSlider, QLabelSlider


def setup_slider(
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
    """Create a QSlider, configure it, and add it to a layout.

    This function creates a horizontal `QSlider`, configures its range, tick size,
    and default value if provided. It connects an optional callback function to the
    slider's `sliderReleased` event and adds the slider to the specified layout.

    Args:
        layout (QLayout): The layout to which the slider will be added.
        minimum (Optional[int], optional): The minimum value of the slider. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the slider. Defaults to None.
        tick_size (Optional[int], optional): The interval between slider ticks. Defaults to None.
        default (Optional[int], optional): The initial value of the slider. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute on slider release. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QSlider widget added to the layout.
    """

    _widget = QSlider()
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


def setup_floatslider(
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
    """Create a QFloatSlider, configure it, and add it to a layout.

    This function creates a `QFloatSlider` widget, sets its precision, range,
    tick size, and default value if provided. It connects an optional callback
    function to the slider's `sliderReleased` signal and adds it to the specified layout.

    Args:
        layout (QLayout): The layout to which the QFloatSlider will be added.
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
        QWidget: The QFloatSlider widget added to the layout.
    """
    _widget = QFloatSlider(digits=digits)
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


def setup_labelslider(
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
    """Create a QLabelSlider, configure it, and add it to a layout.

    This function creates a `QLabelSlider` widget, sets its range, tick size,
    and default value if provided. It connects an optional callback function to
    the slider's `sliderReleased` signal and adds it to the specified layout.

    Args:
        layout (QLayout): The layout to which the QLabelSlider will be added.
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
    _widget = QLabelSlider()

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


def setup_labelfloatslider(
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
    """Create a QFloatLabelSlider, configure it, and add it to a layout.

    This function creates a `QFloatLabelSlider` widget, sets its range, tick size,
    and default value if provided. It connects an optional callback function to
    the slider's `sliderReleased` signal and adds it to the specified layout.

    Args:
        layout (QLayout): The layout to which the QLabelSlider will be added.
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
    _widget = QFloatLabelSlider(digits=digits)

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


def setup_editslider(
    layout: QLayout,
    minimum: Optional[int] = 0,
    maximum: Optional[int] = 100,
    default: Optional[int] = 50,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QEditSlider, configure it, and add it to a layout.

    This function creates a `QEditSlider` widget, sets its range and default value,
    and connects an optional callback function to the `index_changed` signal. It
    then adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QEditSlider will be added.
        minimum (int, optional): The minimum value of the slider. Defaults to 0.
        maximum (int, optional): The maximum value of the slider. Defaults to 100.
        default (int, optional): The initial value of the slider. Defaults to 50.
        function (Optional[Callable], optional): A callback function to execute when the slider value changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QEditSlider widget added to the layout.
    """
    _widget = QEditSlider(min_value=minimum, max_value=maximum, start_value=default)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_editfloatslider(
    layout: QLayout,
    digits: int = 1,
    minimum: Optional[int] = 0,
    maximum: Optional[int] = 1,
    default: Optional[int] = 0.5,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QEditFloatSlider, configure it, and add it to a layout.

    This function creates a `QEditFloatSlider` widget, sets its precision, range,
    and default value. It connects an optional callback function to the `index_changed`
    signal and adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QEditFloatSlider will be added.
        digits (int, optional): The number of decimal places for the float slider. Defaults to 1.
        minimum (float, optional): The minimum value of the slider. Defaults to 0.0.
        maximum (float, optional): The maximum value of the slider. Defaults to 1.0.
        default (float, optional): The initial value of the slider. Defaults to 0.5.
        function (Optional[Callable], optional): A callback function to execute when the slider value changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QEditFloatSlider widget added to the layout.
    """
    _widget = QEditFloatSlider(
        min_value=minimum, max_value=maximum, start_value=default, digits=digits
    )

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
