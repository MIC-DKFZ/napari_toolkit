from typing import Any, Dict, Optional

from napari._qt.qt_resources import QColoredSVGIcon
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QHBoxLayout, QLabel, QWidget


class QIconWrapper(QWidget):
    """A wrapper around a QWidget that adds an icon to visually indicate its status.

    see all options for icon_dict here:
    https://github.com/napari/napari/tree/main/napari/resources/icons

    This widget wraps another QWidget and displays an icon next to it, which changes
    based on the given status. Icons and colors are defined in dictionaries.

    Attributes:
        size (int): The size of the icon.
        icon_dict (Optional[Dict[Any, str]]): A dictionary mapping statuses to icon resources.
        color_dict (Optional[Dict[Any, str]]): A dictionary mapping statuses to colors.
        widget (QWidget): The wrapped widget.
        label (QLabel): The QLabel displaying the status icon.
        status (Optional[Any]): The current status of the widget.
    """

    def __init__(
        self,
        widget: QWidget,
        parent: Optional[QWidget] = None,
        icon_dict: Optional[Dict[Any, str]] = None,
        color_dict: Optional[Dict[Any, str]] = None,
        default: Optional[Any] = None,
        size: int = 24,
    ) -> None:
        """Initializes the QIconWrapper.

        Args:
            widget (QWidget): The main widget to wrap.
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            icon_dict (Optional[Dict[Any, str]], optional): A dictionary mapping statuses to icons. Defaults to None.
            color_dict (Optional[Dict[Any, str]], optional): A dictionary mapping statuses to colors. Defaults to None.
            default (Optional[Any], optional): The default status. Defaults to None.
            size (int, optional): The icon size. Defaults to 24.
        """
        super().__init__(parent)
        self.size = size
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self.icon_dict = icon_dict
        self.color_dict = color_dict

        self.label = QLabel()
        self.label.setContentsMargins(0, 0, 0, 0)
        self.label.setFixedWidth(self.size)
        self.widget = widget

        self._layout.addWidget(self.label)
        self._layout.addWidget(self.widget)

        self.setLayout(self._layout)

        self.status = None
        self.set_status(default)

    def set_status(self, status: Any) -> None:
        """Sets the status of the widget, updating the displayed icon accordingly.

        Args:
            status (Any): The new status to set.
        """
        _icon = QColoredSVGIcon.from_resources(self.icon_dict.get(status, "none"))
        _icon = _icon.colored(color=self.color_dict.get(status, "black"))

        size = self.size  # self.widget.sizeHint().height()

        _icon = _icon.pixmap(QSize(size, size), QIcon.Normal, QIcon.Off)
        self.label.setPixmap(_icon)
        self.status = status

    def __getattr__(self, name, *args, **kwargs):
        """Forwards attribute access to the wrapped widget if not found in QIconWrapper.

        Args:
            name (str): The name of the attribute.

        Returns:
            Any: The requested attribute or method from the wrapped widget.
        """
        target = getattr(self.widget, name)  # target = getattr(self.forward_to, name)
        if callable(target):

            def wrapper(*args, **kwargs):
                print(f"MyClass: Forwarding call to {name} with args={args}, kwargs={kwargs}")
                return target(*args, **kwargs)

            return wrapper
        return target

    def __setattr__(self, name: str, value: Any) -> None:
        """Sets an attribute, forwarding to the wrapped widget if necessary.

        Args:
            name (str): The attribute name.
            value (Any): The value to set.
        """
        try:
            return super().__setattr__(name, value)
        except AttributeError:
            return setattr(self.widget, name, value)

    def __getattribute__(self, name: str) -> Any:
        """Gets an attribute, forwarding to the wrapped widget if necessary.

        Args:
            name (str): The attribute name.

        Returns:
            Any: The attribute value.
        """
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.widget, name)

    def __delattr__(self, name: str) -> None:
        """Deletes an attribute, forwarding to the wrapped widget if necessary.

        Args:
            name (str): The attribute name.
        """
        try:
            return super().__delattr__(name)
        except AttributeError:
            return delattr(self.widget, name)


def setup_icon_wrapper(
    widget: QWidget,
    parent: Optional[QWidget] = None,
    icon_dict: Optional[Dict[Any, str]] = None,
    color_dict: Optional[Dict[Any, str]] = None,
    default: Optional[Any] = None,
    size: int = 24,
) -> QIconWrapper:
    """Creates and adds a QIconWrapper around a given widget.

    see all options for icon_dict here:
    https://github.com/napari/napari/tree/main/napari/resources/icons

    Args:
        widget (QWidget): The widget to wrap.
        parent (Optional[QWidget], optional): The parent widget. Defaults to None.
        icon_dict (Optional[Dict[Any, str]], optional): A dictionary mapping statuses to icons. Defaults to None.
        color_dict (Optional[Dict[Any, str]], optional): A dictionary mapping statuses to colors. Defaults to None.
        default (Optional[Any], optional): The default status. Defaults to None.
        size (int, optional): The icon size. Defaults to 24.

    Returns:
        QIconWrapper: The newly created QIconWrapper instance.
    """
    _layout = widget.parentWidget().layout()
    _widget = QIconWrapper(
        widget, icon_dict=icon_dict, color_dict=color_dict, default=default, size=size
    )
    _layout.addWidget(_widget)
    return _widget
