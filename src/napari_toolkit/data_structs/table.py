from typing import Any, Callable, List, Optional

from qtpy.QtWidgets import QLayout, QSizePolicy, QTableWidget, QTableWidgetItem, QWidget

from napari_toolkit.utils.utils import connect_widget


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
