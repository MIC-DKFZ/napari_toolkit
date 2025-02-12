from typing import Callable, Optional

from qtpy.QtWidgets import QDoubleSpinBox, QLayout, QSpinBox, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_spinbox(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    step_size: Optional[int] = None,
    default: Optional[int] = None,
    function: Optional[Callable] = None,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QSpinBox, configure it, and add it to a layout.

    This function creates a `QSpinBox`, configures its range, step size,
    prefix, suffix, and default value if provided. It connects an optional
    callback function to the spinbox's `valueChanged` event and adds it
    to the specified layout.

    Args:
        layout (QLayout): The layout to which the spinbox will be added.
        minimum (Optional[int], optional): The minimum value of the spinbox. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the spinbox. Defaults to None.
        step_size (Optional[int], optional): The step size for incrementing/decrementing the value. Defaults to None.
        default (Optional[int], optional): The initial value of the spinbox. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the value changes. Defaults to None.
        prefix (Optional[str], optional): Text to display before the spinbox value. Defaults to None.
        suffix (Optional[str], optional): Text to display after the spinbox value. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the spinbox. Defaults to None.
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.

    Returns:
        QWidget: The QSpinBox widget added to the layout.
    """
    _widget = QSpinBox()

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default:
        _widget.setValue(default)
    if step_size is not None:
        _widget.setSingleStep(step_size)
    if suffix is not None:
        _widget.setSuffix(suffix)
    if prefix is not None:
        _widget.setPrefix(prefix)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.valueChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_doublespinbox(
    layout: QLayout,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
    step_size: Optional[float] = None,
    default: Optional[float] = None,
    function: Optional[Callable] = None,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    digits: int = 2,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QDoubleSpinBox, configure it, and add it to a layout.

    This function creates a `QDoubleSpinBox`, configures its range, step size,
    prefix, suffix, number of decimals, and default value if provided. It connects
    an optional callback function to the spinbox's `valueChanged` event and adds
    it to the specified layout.

    Args:
        layout (QLayout): The layout to which the spinbox will be added.
        minimum (Optional[float], optional): The minimum value of the spinbox. Defaults to None.
        maximum (Optional[float], optional): The maximum value of the spinbox. Defaults to None.
        step_size (Optional[float], optional): The step size for incrementing/decrementing the value. Defaults to None.
        default (Optional[float], optional): The initial value of the spinbox. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the value changes. Defaults to None.
        prefix (Optional[str], optional): Text to display before the spinbox value. Defaults to None.
        suffix (Optional[str], optional): Text to display after the spinbox value. Defaults to None.
        digits (int, optional): The number of decimal places to display. Defaults to 2.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the spinbox. Defaults to None.
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.

    Returns:
        QWidget: The QDoubleSpinBox widget added to the layout.
    """
    _widget = QDoubleSpinBox()
    _widget.setDecimals(digits)

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default:
        _widget.setValue(default)
    if step_size is not None:
        _widget.setSingleStep(step_size)
    if suffix is not None:
        _widget.setSuffix(suffix)
    if prefix is not None:
        _widget.setPrefix(prefix)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.valueChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )
