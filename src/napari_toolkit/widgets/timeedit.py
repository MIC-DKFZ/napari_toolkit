from typing import Callable, Optional

from qtpy.QtCore import QDateTime
from qtpy.QtWidgets import QDateTimeEdit, QLayout, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_timeedit(
    layout: QLayout,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates and adds a QDateTimeEdit widget to the specified layout.

    This function initializes a `QDateTimeEdit` widget, sets its default value
    to the current date and time, and connects it to an optional callback function.

    Args:
        layout (QLayout): The layout to which the time edit widget will be added.
        function (Optional[Callable], optional): A callback function triggered when the time changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized `QDateTimeEdit` widget.
    """
    _widget = QDateTimeEdit()
    _widget.setDateTime(QDateTime.currentDateTime())

    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
