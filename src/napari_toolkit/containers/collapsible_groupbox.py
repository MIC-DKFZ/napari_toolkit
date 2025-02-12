# flake8: noqa: E202, E231, E702
from pathlib import Path
from typing import Optional, Tuple

from napari.resources import get_icon_path
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QGroupBox, QHBoxLayout, QLayout, QSizePolicy, QVBoxLayout, QWidget


class QCollapsibleGroupBox(QGroupBox):
    """A collapsible group box that can toggle the visibility of its child widgets.

    This widget extends `QGroupBox` by adding a checkable property, allowing it
    to collapse or expand its contents dynamically.

    Attributes:
        path_right_arrow (str): Path to the right arrow icon (collapsed state).
        path_drop_down (str): Path to the dropdown icon (expanded state).
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initializes the QCollapsibleGroupBox widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)

        self.setCheckable(True)
        self.toggled.connect(self.update)

        path_right_arrow = Path(get_icon_path("right_arrow")).as_posix()
        path_drop_down = Path(get_icon_path("drop_down")).as_posix()

        self.setStyleSheet(
            f"""
            QGroupBox::indicator::unchecked {{
                image: url({path_right_arrow});
                background: transparent;
            }}
            QGroupBox::indicator::checked {{
                image: url({path_drop_down});
                background: transparent;
            }}
        """
        )

    def update(self) -> None:
        """Updates the visibility of child widgets based on the checked state."""
        for widget in self.children():
            if isinstance(widget, QWidget):
                if self.isChecked():
                    widget.show()
                else:
                    widget.hide()

    def childEvent(self, event) -> None:
        """Handles child events to ensure the collapsible state is maintained."""
        super().childEvent(event)
        self.update()


def setup_collapsiblegroupbox(
    layout: Optional[QLayout] = None, text: str = "", collapsed: bool = False
) -> QGroupBox:
    """Creates a collapsible group box and adds it to the provided layout.

    Args:
        layout (Optional[QLayout], optional): The layout to which the group box will be added. Defaults to None.
        text (str, optional): The title text of the group box. Defaults to an empty string.
        collapsed (bool, optional): Whether the group box should start collapsed. Defaults to False.

    Returns:
        QGroupBox: The initialized collapsible group box.
    """
    _widget = QCollapsibleGroupBox(text)
    if layout is not None:
        layout.addWidget(_widget)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    _widget.setChecked(not collapsed)
    return _widget


def setup_vcollapsiblegroupbox(
    layout: Optional[QLayout] = None, text: str = "", collapsed: bool = False
) -> Tuple[QGroupBox, QVBoxLayout]:
    """Creates a collapsible group box with a vertical layout.

    Args:
        layout (Optional[QLayout], optional): The layout to which the group box will be added. Defaults to None.
        text (str, optional): The title text of the group box. Defaults to an empty string.
        collapsed (bool, optional): Whether the group box should start collapsed. Defaults to False.

    Returns:
        Tuple[QGroupBox, QVBoxLayout]: The collapsible group box and its vertical layout.
    """
    _widget = setup_collapsiblegroupbox(layout=layout, text=text, collapsed=collapsed)
    _wlayout = QVBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    _wlayout.setAlignment(Qt.AlignTop)
    return _widget, _wlayout


def setup_hcollapsiblegroupbox(
    layout: Optional[QLayout] = None, text: str = "", collapsed: bool = False
) -> Tuple[QGroupBox, QHBoxLayout]:
    """Creates a collapsible group box with a horizontal layout.

    Args:
        layout (Optional[QLayout], optional): The layout to which the group box will be added. Defaults to None.
        text (str, optional): The title text of the group box. Defaults to an empty string.
        collapsed (bool, optional): Whether the group box should start collapsed. Defaults to False.

    Returns:
        Tuple[QGroupBox, QHBoxLayout]: The collapsible group box and its horizontal layout.
    """
    _widget = setup_collapsiblegroupbox(layout=layout, text=text, collapsed=collapsed)
    _wlayout = QHBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    return _widget, _wlayout
