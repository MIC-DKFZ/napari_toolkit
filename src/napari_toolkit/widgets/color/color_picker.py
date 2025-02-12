from typing import Callable, Optional, Tuple

from qtpy.QtGui import QColor
from qtpy.QtWidgets import QColorDialog, QLayout, QPushButton, QSizePolicy, QWidget

from napari_toolkit.utils.utils import connect_widget


class QColorPicker(QPushButton):
    """A color picker button that opens a color dialog and updates its background color.

    This widget allows users to select a color using a color dialog and updates the button's
    background to match the selected color.

    Attributes:
        color (QColor): The currently selected color.
    """

    def __init__(
        self, initial_color: Tuple[int, int, int] = (255, 255, 255), size: int = 24
    ) -> None:
        """Initializes the QColorPicker widget.

        Args:
            initial_color (Tuple[int, int, int], optional): The initial RGB color. Defaults to white (255, 255, 255).
            size (int, optional): The size of the square button. Defaults to 24.
        """
        super().__init__()

        self.setFixedSize(size, size)  # Make the button square
        self.color = QColor.fromRgb(*initial_color)
        self.update_button_color()
        self.clicked.connect(self.pick_color)

    def pick_color(self) -> None:
        """Opens a color dialog and updates the button color if a valid color is selected."""

        color = QColorDialog.getColor(self.color)
        if color.isValid():
            self.color = color
            self.update_button_color()

    def update_button_color(self) -> None:
        """Updates the button background to reflect the selected color."""
        self.setStyleSheet(f"background-color: {self.color.name()}; border: 1px solid black;")

    def get_color(self) -> Tuple[int, int, int]:
        """Retrieves the currently selected color in RGB format.

        Returns:
            Tuple[int, int, int]: The selected color in (R, G, B) format.
        """
        return self.color.getRgb()[0:3]

    def set_color(self, color: Tuple[int, int, int]) -> None:
        """Sets the button color to the specified RGB value.

        Args:
            color (Tuple[int, int, int]): The new RGB color.
        """
        self.color = QColor.fromRgb(*color)
        self.update_button_color()


def setup_colorpicker(
    layout: QLayout,
    initial_color: Tuple[int] = (255, 255, 255),
    size: int = 24,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates and adds a QColorPicker widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the color picker will be added.
        initial_color (Tuple[int, int, int], optional): The initial RGB color. Defaults to white (255, 255, 255).
        size (int, optional): The size of the color picker button. Defaults to 24.
        function (Optional[Callable[[], None]], optional): A callback function triggered when the color is changed. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized QColorPicker widget.
    """

    _widget = QColorPicker(initial_color, size)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
