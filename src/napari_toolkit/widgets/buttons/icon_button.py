from typing import Callable, Optional

from napari._qt.qt_resources import QColoredSVGIcon
from qtpy.QtCore import QEvent, QObject, QSize
from qtpy.QtGui import QIcon, QPalette
from qtpy.QtWidgets import QLayout, QWidget

from napari_toolkit.widgets.buttons.push_button import setup_pushbutton


def _palette_color_role(name: str):
    """Return a palette role for both legacy and scoped Qt enum APIs."""
    color_role = getattr(QPalette, "ColorRole", None)
    if color_role is not None and hasattr(color_role, name):
        return getattr(color_role, name)
    return getattr(QPalette, name)


class QIconUpdater(QObject):
    """A class that updates a widget's icon color based on its enabled state and theme."""

    def __init__(self, widget: QWidget, icon: QIcon, *args, **kwargs):
        super().__init__(widget, *args, **kwargs)
        self.widget = widget
        self.icon = icon

    def eventFilter(self, obj: QWidget, event: QEvent) -> bool:
        """Filters events for the widget to detect state changes.

        Args:
            obj (QWidget): The object where the event occurred.
            event (QEvent): The event to filter.

        Returns:
            bool: True if the event was handled, False otherwise.
        """
        if obj is self.widget and event.type() == QEvent.EnabledChange:
            self.update_icon(obj)
        return super().eventFilter(obj, event)

    def update_icon(self, obj: QWidget) -> None:
        """Updates the icon color based on the widget's state."""
        palette = obj.palette()

        color_role = _palette_color_role("ButtonText" if self.widget.isEnabled() else "Dark")
        color = palette.color(color_role)
        updated_icon = self.icon.colored(color=color.name())
        self.widget.setIcon(updated_icon)


def setup_icon(_widget: QWidget, icon_name: str, theme: str = "dark") -> QWidget:
    """Sets up an icon for a widget, including dynamic color updates.

    Args:
        _widget (QWidget): The widget to set up the icon for.
        icon_name (str): The resource name of the icon.
        theme (str, optional): The theme to use for the icon ("dark" or "light"). Defaults to "dark".

    Returns:
        QIcon: The configured icon for the widget.
    """

    _icon = QColoredSVGIcon.from_resources(icon_name)
    _icon = _icon.colored(theme=theme)
    _widget.setIcon(_icon)

    size = _widget.sizeHint().height()

    # Keep a Python reference: PySide can garbage-collect an event filter even
    # though it has a Qt parent, after which disabled-state icon updates stop.
    _widget._napari_toolkit_icon_updater = QIconUpdater(_widget, _icon)
    _widget.installEventFilter(_widget._napari_toolkit_icon_updater)
    _widget.setIconSize(QSize(size, size))
    _widget.setFixedHeight(size + 1)

    return _widget


def setup_iconbutton(
    layout: QLayout,
    text: str,
    icon_name: str,
    theme: str = "dark",
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates a push button with an icon and adds it to the specified layout.

    This function first creates a push button using `setup_pushbutton`, then applies
    an icon to it using `setup_icon`.

    Args:
        layout (QLayout): The layout to which the button will be added.
        text (str): The text label of the button.
        icon_name (str): The name of the icon to be applied to the button.
        theme (str, optional): The theme for the icon (e.g., "dark" or "light"). Defaults to "dark".
        function (Optional[Callable], optional): A callback function triggered when the button is clicked. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the button. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized push button with an icon.
    """
    _widget = setup_pushbutton(layout, text, function, tooltips, shortcut, stretch)
    return setup_icon(_widget, icon_name=icon_name, theme=theme)
