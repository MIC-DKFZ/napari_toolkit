from typing import Callable, Optional

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QActionGroup, QLayout, QMenu, QToolButton

from napari_toolkit.utils.utils import connect_widget


def set_options(toolbutton: QToolButton, options: str, default: int = 0) -> None:
    """Set the selected option of a QToolButton's menu by option text.

    Args:
        toolbutton (QToolButton): The tool button created by setup_toolbutton.
        value (str): The option text to select.
    """
    menu = toolbutton.menu()
    menu.clear()
    group = QActionGroup(menu)
    group.setExclusive(True)
    for i, name in enumerate(options):
        act = menu.addAction(name)
        act.setCheckable(True)
        if i == default:
            act.setChecked(True)
        group.addAction(act)


def activate_option(toolbutton: QToolButton, value: str) -> bool:
    """Activate a specific option in a QToolButton menu if it exists.

    Args:
        toolbutton (QToolButton): The tool button created by setup_toolbutton.
        value (str): The option text to activate.

    Returns:
        bool: True if the option was found and activated, False otherwise.
    """
    menu = toolbutton.menu()

    for act in menu.actions():
        if act.text() == value:
            act.setChecked(True)
            # If you also want to trigger the action's signal:
            # act.trigger()
            return True
    return False


def get_option(toolbutton: QToolButton) -> Optional[str]:
    """Return the currently selected option text from a QToolButton menu.

    Args:
        toolbutton (QToolButton): The tool button created by setup_toolbutton.

    Returns:
        Optional[str]: The selected option text, or None if none is selected.
    """
    menu = toolbutton.menu()
    for act in menu.actions():
        if act.isChecked():
            return act.text()

    return None


def setup_toolbutton(
    layout: QLayout,
    options: list[str],
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    default=0,
    stretch: int = 1,
) -> QToolButton:
    """Create a QToolButton with a dropdown menu of exclusive options.

    This function creates a small gear-style QToolButton with a popup menu
    containing a list of selectable options. One option is selected by default,
    and selecting another triggers the provided callback function.

    Args:
        layout (QLayout): The layout to which the tool button will be added.
        options (list[str]): List of option names to show in the menu.
        function (Optional[Callable], optional): Callback function to be called
            when a menu option is triggered. The triggered QAction is passed to the function.
            Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering
            over the button. Defaults to None.
        default (int, optional): Index of the default selected option.
            Defaults to 0.
        stretch (int, optional): Stretch factor for the button in the layout.
            Defaults to 1.

    Returns:
        QToolButton: The configured QToolButton added to the layout.
    """
    _widget = QToolButton()
    _widget.setToolButtonStyle(Qt.ToolButtonIconOnly)
    _widget.setText("⚙")
    _widget.setAutoRaise(True)
    _widget.setPopupMode(QToolButton.InstantPopup)

    menu = QMenu(_widget)
    group = QActionGroup(menu)
    group.setExclusive(True)
    for i, name in enumerate(options):
        act = menu.addAction(name)
        act.setCheckable(True)
        if i == default:
            act.setChecked(True)
        group.addAction(act)
    if function is not None:
        menu.triggered.connect(function)
    _widget.setMenu(menu)
    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=None,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )
