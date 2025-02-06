from typing import Callable, Optional

from qtpy.QtGui import QKeySequence
from qtpy.QtWidgets import QLayout, QShortcut, QWidget


def connect_widget(
    layout: QLayout,
    widget: QWidget,
    widget_event: Optional[Callable] = None,
    function: Optional[Callable] = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """
    Adds a widget to a layout, connects an optional function to a widget event,
    and sets optional tooltips and shortcut.

    Args:
        layout (QLayout): The layout to add the widget to.
        widget (QWidget): The widget to add and configure.
        widget_event (Optional[Callable], optional): The event of the widget to connect the function to.
        function (Optional[Callable], optional): The function to connect to the widget event.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the function.
        tooltips (Optional[str], optional): Tooltip text for the widget.
        stretch (int,optional) Stretch factor of the Widget

    Returns:
        QWidget: The configured widget added to the layout.
    """
    if function and widget_event:
        widget_event.connect(function)
        if shortcut:
            key = QShortcut(QKeySequence(shortcut), widget)
            key.activated.connect(function)

    if tooltips:
        widget.setToolTip(tooltips)

    layout.addWidget(widget, stretch=stretch)
    return widget
