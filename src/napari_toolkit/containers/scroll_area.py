from typing import Optional

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLayout, QScrollArea, QWidget


def setup_scrollarea(
    layout: QLayout,
    widgets: Optional[QWidget] = None,
    max_height: Optional[int] = None,
    max_width: Optional[int] = None,
    stretch: int = 1,
) -> QScrollArea:
    """Creates and configures a QScrollArea, then adds it to the given layout.

    Args:
        layout (QLayout): The parent layout to which the QScrollArea will be added.
        widgets (Optional[QWidget], optional): A widget to be embedded inside the QScrollArea. Defaults to None.
        max_height (Optional[int], optional): Maximum height of the scroll area. Defaults to None.
        max_width (Optional[int], optional): Maximum width of the scroll area. Defaults to None.
        stretch (int, optional): Stretch factor when adding to the layout. Defaults to 1.

    Returns:
        QScrollArea: The configured scroll area widget.
    """
    _widget = QScrollArea()

    if widgets is not None:
        _widget.setWidget(widgets)

    _widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    _widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    if max_height is not None:
        _widget.setMaximumHeight(max_height)
    if max_width is not None:
        _widget.setMaximumWidth(max_width)
    layout.addWidget(_widget, stretch=stretch)
    return _widget
