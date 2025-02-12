from typing import Callable, Optional

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLayout, QSlider, QWidget

from napari_toolkit.utils.utils import connect_widget


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
