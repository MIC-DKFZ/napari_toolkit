from typing import Callable, List, Optional

from qtpy.QtWidgets import QAbstractItemView, QLayout, QListWidget, QSizePolicy, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_list(
    layout: QLayout,
    options: List[str],
    multiple: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QListWidget, configure selection mode, and add it to a layout.

    This function creates a `QListWidget`, populates it with options, and allows
    for either single or multiple selections. It connects an optional callback
    function to the `itemClicked` event.

    Args:
        layout (QLayout): The layout to which the QListWidget will be added.
        options (List[str]): A list of string items to populate the list widget.
        multiple (bool, optional): If True, enables multiple selection mode. Defaults to False.
        function (Optional[Callable], optional): A callback function executed when an item is clicked. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the list widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger an action on the list. Defaults to None.
        stretch (int, optional): The stretch factor for the list widget in the layout. Defaults to 1.

    Returns:
        QWidget: The QListWidget added to the layout.
    """
    _widget = QListWidget()
    _widget.addItems(options)
    if multiple:
        _widget.setSelectionMode(QAbstractItemView.MultiSelection)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.itemClicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
