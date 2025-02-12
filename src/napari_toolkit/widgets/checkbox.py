from typing import Callable, Optional

from qtpy.QtWidgets import QCheckBox, QLayout, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_checkbox(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QCheckBox, configure it, and add it to a layout.

    This function creates a `QCheckBox` widget, sets its initial checked state,
    and connects an optional callback function to the `stateChanged` signal.
    It then adds the checkbox to the specified layout.

    Args:
        layout (QLayout): The layout to which the QCheckBox will be added.
        text (str): The text label for the checkbox.
        checked (bool): The initial checked state of the checkbox. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the `stateChanged` signal is triggered. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the checkbox. Defaults to None.
        stretch (int, optional): The stretch factor for the checkbox in the layout. Defaults to 1.

    Returns:
        QWidget: The QCheckBox widget added to the layout.
    """
    _widget = QCheckBox(text)
    _widget.setChecked(checked)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.stateChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )
