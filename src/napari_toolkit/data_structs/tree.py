from typing import Callable, List, Optional

from qtpy.QtWidgets import QAbstractItemView, QLayout, QSizePolicy, QTreeWidget, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_tree(
    layout: QLayout,
    header: Optional[List[str]] = None,
    multiple: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QTreeWidget, configure selection mode, and add it to a layout.

    This function creates a `QTreeWidget`, sets optional column headers, and allows
    for either single or multiple selections. It connects an optional callback
    function to the `itemClicked` event.

    Example usage:
        ```python
        from qtpy.QtWidgets import QTreeWidgetItem

        tree = setup_tree(layout, header=["Name", "Value"])
        parent = QTreeWidgetItem(tree, ["Parent Item", "10"])
        child1 = QTreeWidgetItem(parent, ["Child 1", "20"])
        child2 = QTreeWidgetItem(parent, ["Child 2", "30"])
        ```

    Args:
        layout (QLayout): The layout to which the QTreeWidget will be added.
        header (Optional[List[str]], optional): A list of column headers for the tree widget. Defaults to None.
        multiple (bool, optional): If True, enables multiple selection mode. Defaults to False.
        function (Optional[Callable], optional): A callback function executed when an item is clicked. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the tree widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger an action on the tree widget. Defaults to None.
        stretch (int, optional): The stretch factor for the tree widget in the layout. Defaults to 1.

    Returns:
        QWidget: The QTreeWidget added to the layout.
    """

    _widget = QTreeWidget()
    if header is not None:
        _widget.setHeaderLabels(header)
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
