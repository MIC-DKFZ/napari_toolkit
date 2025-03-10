from typing import Callable, Optional

import numpy as np
from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import QHBoxLayout, QLayout, QLineEdit, QPushButton, QSlider, QWidget

from napari_toolkit.utils.utils import connect_widget
from napari_toolkit.widgets.sliders.double_slider import QDoubleSlider


class QEditSlider(QWidget):
    """A slider with an editable text field for integer values.

    This widget extends a `QSlider` by adding a `QLineEdit` for manual input
    and optional increment/decrement buttons.

    Attributes:
        index_changed (Signal): A signal emitted when the slider value changes.
        min_value (int): The minimum allowed value.
        max_value (int): The maximum allowed value.
        current_value (int): The current value of the slider.
    """

    index_changed = Signal()

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        min_value: int = 0,
        max_value: int = 100,
        start_value: int = 0,
        include_buttons: bool = True,
    ) -> None:
        """Initializes the QEditSlider widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            min_value (int, optional): The minimum value of the slider. Defaults to 0.
            max_value (int, optional): The maximum value of the slider. Defaults to 100.
            start_value (int, optional): The initial value of the slider. Defaults to 0.
            include_buttons (bool, optional): Whether to include increment/decrement buttons. Defaults to True.
        """
        super().__init__(parent)

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = start_value

        self.init_ui(include_buttons)
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self, include_buttons: bool) -> None:
        """Initializes the UI components.

        Args:
            include_buttons (bool): Whether to include increment/decrement buttons.
        """
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(self.min_value)
        self.slider.setMaximum(self.max_value)
        self.slider.setValue(self.current_value)
        self.slider.valueChanged.connect(self.update_edit)
        self.slider.sliderReleased.connect(self.update_progress)
        self.slider.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.current_value))
        self.line_edit.returnPressed.connect(self.update_progress)
        self.line_edit.setContentsMargins(0, 0, 0, 0)
        if include_buttons:
            self.next_button = QPushButton("+", self)
            self.next_button.clicked.connect(self.increment_value)
            self.next_button.setContentsMargins(0, 0, 0, 0)

            self.prev_button = QPushButton("-", self)
            self.prev_button.clicked.connect(self.decrement_value)
            self.prev_button.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.slider, stretch=10)
        if include_buttons:
            layout.addWidget(self.prev_button, stretch=2)
        layout.addWidget(self.line_edit, stretch=3)
        if include_buttons:
            layout.addWidget(self.next_button, stretch=2)

        self.setLayout(layout)

    def update_edit(self) -> None:
        """Updates the line edit field when the slider value changes."""
        try:
            value = int(self.slider.value())
            self.line_edit.setText(str(value))
        except ValueError:
            pass

    def update_progress(self) -> None:
        """Updates the slider value when a new value is entered in the line edit."""

        try:
            value = int(self.line_edit.text())
            self.setValue(value)
        except ValueError:
            pass

    def setValue(self, value: int) -> None:
        """Sets the slider and line edit to a new value.

        Ensures the value is within the allowed range before updating.

        Args:
            value (int): The new value to set.
        """
        if self.min_value <= value <= self.max_value:
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.slider.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self) -> None:
        """Increments the slider value by 1."""
        self.setValue(self.current_value + 1)

    def decrement_value(self) -> None:
        """Decrements the slider value by 1."""
        self.setValue(self.current_value - 1)

    def value(self):
        return self.current_value


class QEditDoubleSlider(QWidget):
    """A slider with an editable text field for floating-point values.

    This widget extends a `QDoubleSlider` by adding a `QLineEdit` for manual
    input and optional increment/decrement buttons.

    Attributes:
        index_changed (Signal): A signal emitted when the slider value changes.
        digits (int): The number of decimal places retained.
        digit_factor (int): The factor used for internal scaling.
        min_value (float): The minimum allowed value.
        max_value (float): The maximum allowed value.
        current_value (float): The current value of the slider.
    """

    index_changed = Signal()

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        min_value: float = 0,
        max_value: float = 100,
        start_value: float = 0,
        digits: int = 1,
        include_buttons: bool = True,
    ) -> None:
        """Initializes the QEditDoubleSlider widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            min_value (float, optional): The minimum value of the slider. Defaults to 0.
            max_value (float, optional): The maximum value of the slider. Defaults to 100.
            start_value (float, optional): The initial value of the slider. Defaults to 0.
            digits (int, optional): The number of decimal places to retain. Defaults to 1.
            include_buttons (bool, optional): Whether to include increment/decrement buttons. Defaults to True.
        """
        super().__init__(parent)
        self.digits = digits
        self.digit_factor = 10**digits

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = start_value
        self.init_ui(include_buttons)
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self, include_buttons: bool) -> None:
        """Initializes the UI components.

        Args:
            include_buttons (bool): Whether to include increment/decrement buttons.
        """
        self.slider = QDoubleSlider(self, digits=self.digits)
        self.slider.setOrientation(Qt.Horizontal)

        self.slider.setMinimum(self.min_value)
        self.slider.setMaximum(self.max_value)
        self.slider.setValue(self.current_value)

        self.slider.valueChanged.connect(self.update_edit)
        self.slider.sliderReleased.connect(self.update_progress)
        self.slider.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.current_value))
        self.line_edit.returnPressed.connect(self.update_progress)
        self.line_edit.setContentsMargins(0, 0, 0, 0)

        if include_buttons:
            self.next_button = QPushButton("+", self)
            self.next_button.clicked.connect(self.increment_value)
            self.next_button.setContentsMargins(0, 0, 0, 0)

            self.prev_button = QPushButton("-", self)
            self.prev_button.clicked.connect(self.decrement_value)
            self.prev_button.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.slider, stretch=10)
        if include_buttons:
            layout.addWidget(self.prev_button, stretch=2)
        layout.addWidget(self.line_edit, stretch=3)
        if include_buttons:
            layout.addWidget(self.next_button, stretch=2)

        self.setLayout(layout)

    def update_edit(self) -> None:
        """Updates the line edit field when the slider value changes."""
        try:
            value = self.slider.value()
            self.line_edit.setText(str(value))
        except ValueError:
            pass

    def update_progress(self) -> None:
        """Updates the slider value when a new value is entered in the line edit."""
        try:
            value = float(self.line_edit.text())
            self.setValue(value)
        except ValueError:
            pass

    def setValue(self, value: float) -> None:
        """Sets the slider and line edit to a new value.

        Ensures the value is within the allowed range before updating.

        Args:
            value (float): The new value to set.
        """
        if self.min_value <= value <= self.max_value:
            value = np.round(value, self.digits)
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.slider.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self) -> None:
        """Increments the slider value by the smallest allowed step."""
        self.setValue(self.current_value + 10 ** (-self.digits))

    def decrement_value(self) -> None:
        """Decrements the slider value by the smallest allowed step."""
        self.setValue(self.current_value - 10 ** (-self.digits))

    def value(self):
        return self.current_value


def setup_editslider(
    layout: QLayout,
    minimum: Optional[int] = 0,
    maximum: Optional[int] = 100,
    default: Optional[int] = 50,
    include_buttons: bool = True,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QEditSlider, configure it, and add it to a layout.

    This function creates a `QEditSlider` widget, sets its range and default value,
    and connects an optional callback function to the `index_changed` signal. It
    then adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QEditSlider will be added.
        minimum (int, optional): The minimum value of the slider. Defaults to 0.
        maximum (int, optional): The maximum value of the slider. Defaults to 100.
        default (int, optional): The initial value of the slider. Defaults to 50.
        include_buttons(boot): Include a next and previous button next to the slider. Defaults to True.
        function (Optional[Callable], optional): A callback function to execute when the slider value changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QEditSlider widget added to the layout.
    """
    _widget = QEditSlider(
        min_value=minimum, max_value=maximum, start_value=default, include_buttons=include_buttons
    )

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_editdoubleslider(
    layout: QLayout,
    digits: int = 1,
    minimum: Optional[int] = 0,
    maximum: Optional[int] = 1,
    default: Optional[int] = 0.5,
    include_buttons: bool = True,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QEditDoubleSlider, configure it, and add it to a layout.

    This function creates a `QEditDoubleSlider` widget, sets its precision, range,
    and default value. It connects an optional callback function to the `index_changed`
    signal and adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QEditDoubleSlider will be added.
        digits (int, optional): The number of decimal places for the float slider. Defaults to 1.
        minimum (float, optional): The minimum value of the slider. Defaults to 0.0.
        maximum (float, optional): The maximum value of the slider. Defaults to 1.0.
        default (float, optional): The initial value of the slider. Defaults to 0.5.
        include_buttons(boot): Include a next and previous button next to the slider. Defaults to True.
        function (Optional[Callable], optional): A callback function to execute when the slider value changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QEditFloatSlider widget added to the layout.
    """
    _widget = QEditDoubleSlider(
        min_value=minimum,
        max_value=maximum,
        start_value=default,
        digits=digits,
        include_buttons=include_buttons,
    )

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
