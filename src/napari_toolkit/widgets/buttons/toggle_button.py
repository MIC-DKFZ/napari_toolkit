from typing import Callable, Optional

from qtpy.QtWidgets import QLayout, QPushButton, QWidget

from napari_toolkit.utils.theme import connect_theme_change, get_theme_colors
from napari_toolkit.utils.utils import connect_widget


class QToggleButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None):
        """Initializes the toggle button.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setCheckable(True)  # Makes it toggleable
        self.clicked.connect(self.toggle_button)
        self.set_color()
        connect_theme_change(self.on_theme_change)

    def toggle_button(self):
        if self.isChecked():
            # self.setStyleSheet("background-color:  rgb(0,100, 167);")
            self.setStyleSheet(f"background-color:  {self.highlight_color};")
        else:
            self.setStyleSheet("")

    def set_color(self):
        theme_colors = get_theme_colors()
        self.highlight_color = theme_colors.highlight

    def on_theme_change(self, *args, **kwargs):
        self.set_color()
        self.setStyleSheet(f"background-color: {self.highlight_color};")


def setup_togglebutton(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QToggleButton, configure it, and add it to a layout.

    This function creates a `QToggleButton` widget, sets its initial checked state,
    and connects an optional callback function to its `clicked` signal. It also adds
    the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QToggleButton will be added.
        text (str): The text label for the toggle button.
        checked (bool, optional): The initial checked state of the toggle button. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the button is clicked. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the button. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the button. Defaults to None.
        stretch (int, optional): The stretch factor for the button in the layout. Defaults to 1.

    Returns:
        QWidget: The QToggleButton widget added to the layout.
    """

    _widget = QToggleButton(text)
    _widget.setChecked(checked)
    _widget.toggle_button()

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
