import re
from typing import Callable, Optional, Tuple

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QHBoxLayout, QLayout, QSizePolicy, QWidget

from napari_toolkit.utils.utils import connect_widget
from napari_toolkit.widgets.color.color_picker import setup_colorpicker
from napari_toolkit.widgets.sliders.edit_slider import setup_editdoubleslider
from napari_toolkit.widgets.text_edit import setup_lineedit


class QEditColorPicker(QWidget):
    """A widget that combines a color picker, RGB input field, and opacity slider.

    This widget allows users to select a color using a color picker, manually enter
    RGB values, and adjust opacity using a slider.

    Attributes:
        changed (Signal): A signal emitted when the color or opacity changes.
        colorpicker (QWidget): The embedded color picker.
        RGB_edit (QWidget): A line edit for entering RGB values.
        oppacity_slider (QWidget): A slider for adjusting opacity.
    """

    changed = Signal()

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        initial_color: Tuple[int, int, int] = (255, 255, 255),
    ):
        """Initializes the QEditColorPicker widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            initial_color (Tuple[int, int, int], optional): The initial RGB color. Defaults to white (255, 255, 255).
        """
        super().__init__(parent)
        self._layout = QHBoxLayout()

        self.colorpicker = setup_colorpicker(
            self._layout, initial_color=initial_color, size=24, function=self.update_lineedit
        )

        self.RGB_edit = setup_lineedit(self._layout, function=self.update_picker)
        self.RGB_edit.setFixedWidth(85)
        self.update_lineedit()

        self.oppacity_slider = setup_editdoubleslider(
            self._layout, 2, 0, 1, default=1.0, include_buttons=False, function=self.changed.emit
        )
        self.oppacity_slider.line_edit.setFixedWidth(35)

        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)

    def update_lineedit(self):
        """Updates the RGB input field based on the selected color from the color picker."""
        color = self.colorpicker.get_color()
        self.RGB_edit.setText(f"{color[0]}, {color[1]}, {color[2]}")
        self.changed.emit()

    def update_picker(self):
        """Updates the color picker based on the entered RGB values in the input field.

        If values are in the 0-1 range, they are converted to 0-255.
        """
        values = re.findall(r"[-+]?\d*\.\d+|\d+", self.RGB_edit.text())
        if len(values) != 3:
            return

        r, g, b = map(float, values)

        # Check if values are in 0-1 range, convert to 0-255 if necessary
        if 0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1:
            color = [int(r * 255), int(g * 255), int(b * 255)]
            self.RGB_edit.setText(f"{color[0]}, {color[1]}, {color[2]}")
        else:
            color = [int(r), int(g), int(b)]
        self.colorpicker.set_color(color)
        self.changed.emit()

    def get_rgb(self):
        """Gets the current RGB color.

        Returns:
            Tuple[int, int, int]: The selected color in (R, G, B) format.
        """
        return self.colorpicker.get_color()

    def get_color(self):
        """Gets the current RGBA color, including opacity.

        Returns:
            Tuple[int, int, int, float]: The selected color in (R, G, B, A) format.
        """
        return [*self.colorpicker.get_color(), self.oppacity_slider.current_value]

    def get_oppacity(self):
        """Gets the current opacity value.

        Returns:
            float: The selected opacity (0-1).
        """
        return self.oppacity_slider.current_value

    def set_color(self, color: Tuple[int, int, int]) -> None:
        """Sets the button color to the specified RGB value.

        Args:
            color (Tuple[int, int, int]): The new RGB color.
        """
        if len(color) == 4:
            self.set_oppacity(color[3])
            color = color[:3]
        self.colorpicker.set_color(color)
        self.update_lineedit()

    def set_oppacity(self, oppacity: float) -> None:
        self.oppacity_slider.setValue(oppacity)


def setup_editcolorpicker(
    layout: QLayout,
    initial_color: Tuple[int, int, int] = (255, 255, 255),
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates and adds a QEditColorPicker to the given layout.

    Args:
        layout (QLayout): The layout to which the widget will be added.
        initial_color (Tuple[int, int, int], optional): The initial RGB color. Defaults to white (255, 255, 255).
        function (Optional[Callable], optional): A callback function triggered when the value changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized QEditColorPicker instance.
    """

    _widget = QEditColorPicker(initial_color=initial_color)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
