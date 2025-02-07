from typing import Callable, Optional

from qtpy.QtWidgets import QLayout, QPushButton, QRadioButton, QWidget

from napari_toolkit.setup.utils import connect_widget
from napari_toolkit.widgets.toggle_button import QToggleButton


def setup_button(
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


def setup_radiobutton(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QRadioButton, configure it, and add it to a layout.

    This function creates a `QRadioButton` widget, sets its initial checked state,
    and connects an optional callback function to the `toggled` signal.
    It then adds the radio button to the specified layout.

    Args:
        layout (QLayout): The layout to which the QRadioButton will be added.
        text (str): The text label for the radio button.
        checked (bool): The initial checked state of the radio button. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the `toggled` signal is triggered. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the radio button. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the radio button. Defaults to None.
        stretch (int, optional): The stretch factor for the radio button in the layout. Defaults to 1.

    Returns:
        QWidget: The QRadioButton widget added to the layout.
    """

    _widget = QRadioButton(text)
    _widget.setChecked(checked)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.toggled,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_togglebutton(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QToggleButton, configure it, and add it to a layout.

    This function creates a `QToggleButton` widget, sets its initial checked state,
    and connects an optional callback function to its `clicked` signal. It also adds
    the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QToggleButton will be added.
        text (str): The text label for the toggle button.
        checked (bool, optional): The initial checked state of the toggle button. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the button is clicked. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the button. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the button. Defaults to None.
        stretch (int, optional): The stretch factor for the button in the layout. Defaults to 1.

    Returns:
        QWidget: The QToggleButton widget added to the layout.
    """

    _widget = QToggleButton(text)
    _widget.setChecked(checked)
    _widget.toggle_button()

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
