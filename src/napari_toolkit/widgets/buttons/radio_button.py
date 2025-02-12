from typing import Callable, Optional

from qtpy.QtWidgets import QLayout, QRadioButton, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_radiobutton(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QRadioButton, configure it, and add it to a layout.

    This function creates a `QRadioButton` widget, sets its initial checked state,
    and connects an optional callback function to the `toggled` signal.
    It then adds the radio button to the specified layout.

    Args:
        layout (QLayout): The layout to which the QRadioButton will be added.
        text (str): The text label for the radio button.
        checked (bool): The initial checked state of the radio button. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the `toggled` signal is triggered. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the radio button. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the radio button. Defaults to None.
        stretch (int, optional): The stretch factor for the radio button in the layout. Defaults to 1.

    Returns:
        QWidget: The QRadioButton widget added to the layout.
    """

    _widget = QRadioButton(text)
    _widget.setChecked(checked)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.toggled,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
