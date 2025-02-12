from typing import List, Optional

from qtpy.QtWidgets import QLayout, QSizePolicy, QTabWidget, QWidget


def setup_tabwidget(
    layout: QLayout,
    widgets: Optional[List[QWidget]] = None,
    page_names: Optional[List[str]] = None,
    stretch: int = 1,
) -> QTabWidget:
    """Creates a QTabWidget, adds it to the given layout, and populates it with tabs.

    Args:
        layout (QLayout): The parent layout to which the QTabWidget will be added.
        widgets (Optional[List[QWidget]], optional): A list of widgets to be added as tabs. Defaults to None.
        page_names (Optional[List[str]], optional): A list of tab names corresponding to the widgets. Defaults to None.
        stretch (int, optional): Stretch factor when adding to the layout. Defaults to 1.

    Returns:
        QTabWidget: The configured tab widget with the specified pages.
    """
    _widget = QTabWidget()
    if widgets is not None and page_names is not None:
        for widget, name in zip(widgets, page_names):
            _widget.addTab(widget, name)

    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    layout.addWidget(_widget, stretch=stretch)
    return _widget
