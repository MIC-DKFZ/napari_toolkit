from typing import Callable, List, Optional

from qtpy.QtGui import QKeySequence
from qtpy.QtWidgets import QLayout, QShortcut, QWidget

from napari_toolkit.setup.utils import connect_widget
from napari_toolkit.widgets.switch import QHSwitch, QVSwitch


def _setup_switch(
    _widget: QWidget,
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: Optional[int] = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
) -> QWidget:
    """Configure a switch-like widget, set options, and add it to a layout.

    This function configures a `_widget` (assumed to be a custom switch-like widget),
    populates it with options, sets a default value if provided, and assigns an optional
    callback function to the `clicked` event. A shortcut key can be assigned to toggle
    through the options.

    Args:
        _widget (QWidget): The widget to configure and add to the layout.
        layout (QLayout): The layout to which the widget will be added.
        options (List[str]): A list of string options for the switch widget.
        function (Optional[Callable[[str], None]], optional): A callback function that takes the selected option as an argument. Defaults to None.
        default (Optional[int], optional): The index of the default selected option. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to toggle the switch. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.

    Returns:
        QWidget: The configured switch widget added to the layout.
    """
    _widget.addItems(options)

    if default is not None:
        _widget._check(default)

    if shortcut:
        key = QShortcut(QKeySequence(shortcut), _widget)
        key.activated.connect(_widget.next)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=None,
        tooltips=tooltips,
    )


def setup_vswitch(
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
):
    """Create a vertical switch widget (QVSwitch), configure it, and add it to a layout.

    This function creates a `QVSwitch` widget, populates it with options, sets a default
    selection if provided, and connects an optional callback function. A shortcut key
    can be assigned to toggle between options.

    Args:
        layout (QLayout): The layout to which the QVSwitch will be added.
        options (List[str]): A list of string options for the switch widget.
        function (Optional[Callable[[str], None]], optional): A callback function that takes the selected option as an argument. Defaults to None.
        default (Optional[int], optional): The index of the default selected option. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to toggle the switch. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.

    Returns:
        QWidget: The configured QVSwitch widget added to the layout.
    """
    _widget = QVSwitch()
    return _setup_switch(_widget, layout, options, function, default, shortcut, tooltips)


def setup_hswitch(
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
):
    """Create a horizontal switch widget (QHSwitch), configure it, and add it to a layout.

    This function creates a `QHSwitch` widget, populates it with options, sets a default
    selection if provided, and connects an optional callback function. A shortcut key
    can be assigned to toggle between options.

    Args:
        layout (QLayout): The layout to which the QHSwitch will be added.
        options (List[str]): A list of string options for the switch widget.
        function (Optional[Callable[[str], None]], optional): A callback function that takes the selected option as an argument. Defaults to None.
        default (Optional[int], optional): The index of the default selected option. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to toggle the switch. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.

    Returns:
        QWidget: The configured QHSwitch widget added to the layout.
    """
    _widget = QHSwitch()
    return _setup_switch(_widget, layout, options, function, default, shortcut, tooltips)
