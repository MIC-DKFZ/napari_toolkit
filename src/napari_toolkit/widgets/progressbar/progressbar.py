from typing import Optional

from qtpy.QtWidgets import QLayout, QProgressBar, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_progressbar(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    default: Optional[int] = None,
    percentage: bool = False,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QProgressBar, configure it, and add it to a layout.

    This function creates a `QProgressBar` widget, sets its range, default value,
    and whether or not to display the percentage text. It adds the widget to the
    specified layout.

    Args:
        layout (QLayout): The layout to which the QProgressBar will be added.
        minimum (Optional[int], optional): The minimum value of the progress bar. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the progress bar. Defaults to None.
        default (Optional[int], optional): The initial value of the progress bar. Defaults to None.
        percentage (bool, optional): If True, shows percentage text on the progress bar. Defaults to False.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the progress bar. Defaults to None.
        stretch (int, optional): The stretch factor for the progress bar in the layout. Defaults to 1.

    Returns:
        QWidget: The QProgressBar widget added to the layout.
    """
    _widget = QProgressBar()
    _widget.setTextVisible(percentage)

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default:
        _widget.setValue(default)

    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=None,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )
