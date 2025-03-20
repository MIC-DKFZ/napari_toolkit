from typing import Callable, List, Optional

from qtpy.QtWidgets import QComboBox, QLayout, QWidget

from napari_toolkit.utils.utils import connect_widget


def setup_combobox(
    layout: QLayout,
    options: List[str],
    placeholder: Optional[str] = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QComboBox, configure it, and add it to a layout.

    This function creates a `QComboBox` widget, populates it with a list of options,
    sets a placeholder if provided, and connects an optional callback function
    to the `currentTextChanged` signal. It then adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QComboBox will be added.
        options (List[str]): A list of string options to populate the combo box.
        placeholder (Optional[str], optional): Placeholder text for the combo box. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the `currentTextChanged` signal is triggered. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the combo box. Defaults to None.
        stretch (int, optional): The stretch factor for the combo box in the layout. Defaults to 1.

    Returns:
        QWidget: The QComboBox widget added to the layout.
    """

    _widget = QComboBox()
    _widget.addItems(options)

    if placeholder is not None:
        _widget.setPlaceholderText(placeholder)
    _widget.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.currentTextChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )
