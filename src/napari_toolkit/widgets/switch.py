from typing import Any, Callable, List, Optional

from qtpy.QtCore import Signal
from qtpy.QtGui import QKeySequence
from qtpy.QtWidgets import QHBoxLayout, QLayout, QPushButton, QShortcut, QVBoxLayout, QWidget

from napari_toolkit.utils.theme import connect_theme_change, get_theme_colors
from napari_toolkit.utils.utils import connect_widget


class _QSwitch(QWidget):
    """A widget that provides a toggleable switch with multiple button options."""

    clicked = Signal()

    def __init__(self, parent=None, fixed_color=None):
        super().__init__(parent)
        self.fixed_color = fixed_color

        self.buttons = []
        self.options = []
        self.value = None
        self.index = None
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)

        self.set_color()
        connect_theme_change(self.on_theme_change)

    def addItems(self, items):
        """Add Items as buttons to the widget"""
        for i, item in enumerate(items):
            _btn = QPushButton(item)
            _btn.clicked.connect(lambda _, idx=i: self._on_button_pressed(idx))
            self._layout.addWidget(_btn)
            self.buttons.append(_btn)
            self.options.append(item)

    def _on_button_pressed(self, idx: int):
        """
        Handles the button press event, updating the selected option.

        Args:
            idx (int): Index of the button pressed.
        """
        self._uncheck()
        self._check(idx)
        self.clicked.emit()

    def _uncheck(self):
        """Unchecks all buttons and resets the selection state."""
        self.value = None
        self.index = None
        for btn in self.buttons:
            btn.setChecked(False)
            btn.setStyleSheet("")

    def _check(self, idx: int):
        """
        Checks the button at the specified index and updates the selection state.

        Args:
            idx (int): Index of the button to check.
        """
        if idx is not None and 0 <= idx < len(self.buttons):
            self.value = self.options[idx]
            self.index = idx
            self.buttons[idx].setChecked(True)

            # self.setStyleSheet("background-color:  rgb(0,100, 167);")
            self.buttons[idx].setStyleSheet(f"background-color: {self.highlight_color};")

    def next(self, *args, **kwargs):
        """Just go to the next item"""
        idx = (self.index + 1) % len(self.options)
        self._on_button_pressed(idx)

    def set_color(self):
        if self.fixed_color is not None:
            self.highlight_color = self.fixed_color
        else:
            theme_colors = get_theme_colors()
            self.highlight_color = theme_colors.highlight

    def on_theme_change(self, *args, **kwargs):
        self.set_color()
        if self.index is not None:
            self.buttons[self.index].setStyleSheet(f"background-color: {self.highlight_color};")

    def currentText(self):
        return self.buttons[self.index].text()

    def currentIndex(self):
        return self.index

    def setCurrentIndex(self, value):
        self._uncheck()
        self._check(value)
        self.clicked.emit()

    def findText(self, value):
        try:
            return self.options.index(value)
        except ValueError:
            return -1


class QHSwitch(_QSwitch):
    """
    A horizontal switch widget with multiple button options.

    Args:
        options (List[str]): List of option names for each button.
        function (Callable[[], None]): Function to call when a button is pressed.
        default (Optional[int], optional): Index of the default selected option. Defaults to None.
        shortcuts (Optional[List[str]], optional): List of keyboard shortcuts for each option. Defaults to None.
    """

    def __init__(self, parent=None, fixed_color=None):
        self._layout = QHBoxLayout()
        super().__init__(parent, fixed_color)


class QVSwitch(_QSwitch):
    """
    A vertical switch widget with multiple button options.

    Args:
        options (List[str]): List of option names for each button.
        function (Callable[[], None]): Function to call when a button is pressed.
        default (Optional[int], optional): Index of the default selected option. Defaults to None.
        shortcuts (Optional[List[str]], optional): List of keyboard shortcuts for each option. Defaults to None.
    """

    def __init__(self, parent=None, fixed_color=None):
        self._layout = QVBoxLayout()
        super().__init__(parent, fixed_color)


def _setup_switch(
    _widget: QWidget,
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: Optional[int] = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
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
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.

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
        stretch=stretch,
    )


def setup_vswitch(
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    fixed_color: Optional[Any] = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
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
        fixed_color: Optiona[Any]: qt Color information. If given this oneis used, else the theme color.
        shortcut (Optional[str], optional): A keyboard shortcut to toggle the switch. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.
    Returns:
        QWidget: The configured QVSwitch widget added to the layout.
    """
    _widget = QVSwitch(fixed_color=fixed_color)
    return _setup_switch(_widget, layout, options, function, default, shortcut, tooltips, stretch)


def setup_hswitch(
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    fixed_color: Optional[Any] = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
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
        If given this oneis used, else the theme color
        shortcut (Optional[str], optional): A keyboard shortcut to toggle the switch. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.

    Returns:
        QWidget: The configured QHSwitch widget added to the layout.
    """
    _widget = QHSwitch(fixed_color=fixed_color)
    return _setup_switch(_widget, layout, options, function, default, shortcut, tooltips, stretch)
