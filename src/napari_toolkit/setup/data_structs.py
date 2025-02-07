from typing import Any, Callable, List, Optional

from qtpy.QtWidgets import (
    QAbstractItemView,
    QLayout,
    QListWidget,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QWidget,
)

from napari_toolkit.setup.utils import connect_widget


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


def setup_table(
    layout: QLayout,
    data: List[List[Any]],
    header: Optional[List[str]] = None,
    show_index=True,
    editable=False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QTableWidget, populate it with data, and add it to a layout.

    This function creates a `QTableWidget`, sets optional headers, and fills the table
    with provided data. It also allows configuring whether the table is editable
    and whether to show the row index.

    Example usage:
        ```python
            table.setItem(0, 0, QTableWidgetItem("Row 1, Col 1"))
            table.setItem(0, 1, QTableWidgetItem("Row 1, Col 2"))
            table.setItem(1, 0, QTableWidgetItem("Row 2, Col 1"))
            table.setItem(1, 1, QTableWidgetItem("Row 2, Col 2"))
        ```
    Args:
        layout (QLayout): The layout to which the QTableWidget will be added.
        data (List[List[Any]]): A 2D list containing table data.
        header (Optional[List[str]], optional): A list of column headers. Defaults to None.
        show_index (bool, optional): Whether to display the row index. Defaults to True.
        editable (bool, optional): If False, disables table editing. Defaults to False.
        function (Optional[Callable], optional): A callback function executed when interacting with the table. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the table. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger an action on the table. Defaults to None.
        stretch (int, optional): The stretch factor for the table in the layout. Defaults to 1.

    Returns:
        QWidget: The QTableWidget added to the layout.
    """

    _widget = QTableWidget()
    if header is not None:
        _widget.setColumnCount(len(header))
        _widget.setHorizontalHeaderLabels(header)

    if data is not None:
        _widget.setRowCount(len(data))
        for i, di in enumerate(data):
            for j, _dj in enumerate(di):
                _widget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
    _widget.resizeColumnsToContents()
    if not editable:
        _widget.setEditTriggers(QTableWidget.NoEditTriggers)
    _widget.verticalHeader().setVisible(show_index)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
