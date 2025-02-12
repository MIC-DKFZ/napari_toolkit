from typing import Callable, Optional

from qtpy.QtWidgets import QLayout, QPushButton, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_pushbutton(
    layout: QLayout,
    text: str,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QPushButton, configure it, and add it to a layout.

    This function creates a QPushButton with the specified text, connects it
    to an optional callback function, sets tooltips and shortcuts if provided,
    and adds it to the given layout with the specified stretch factor.

    Args:
        layout (QLayout): The layout to which the button will be added.
        text (str): The text to display on the button.
        function (Optional[Callable], optional): The function to connect to the button's `clicked` event.
            Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the button.
            Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the button. Defaults to None.
        stretch (int, optional): The stretch factor for the button in the layout. Defaults to 1.

    Returns:
        QWidget: The QPushButton widget added to the layout.
    """

    _widget = QPushButton(text)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
