from typing import Callable, Optional

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QHBoxLayout, QLayout, QLineEdit, QProgressBar, QPushButton, QWidget

from napari_toolkit.utils.utils import connect_widget


class QProgressbarEdit(QWidget):
    """A progress bar with an editable text field and increment/decrement buttons.

    This widget extends a `QProgressBar` by adding a `QLineEdit` for manual input
    and increment/decrement buttons to adjust the value.

    Attributes:
        index_changed (Signal): A signal emitted when the progress value changes.
        min_value (int): The minimum allowed value.
        max_value (int): The maximum allowed value.
        current_value (int): The current value of the progress bar.
    """

    index_changed = Signal()

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        min_value: int = 0,
        max_value: int = 100,
        start_value: int = 0,
    ) -> None:
        """Initializes the QProgressbarEdit widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            min_value (int, optional): The minimum value of the progress bar. Defaults to 0.
            max_value (int, optional): The maximum value of the progress bar. Defaults to 100.
            start_value (int, optional): The initial value of the progress bar. Defaults to 0.
        """
        super().__init__(parent)

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = start_value
        self.init_ui()
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self) -> None:
        """Initializes the UI components."""
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(self.min_value)
        self.progress_bar.setMaximum(self.max_value)
        self.progress_bar.setValue(self.current_value)
        self.progress_bar.setFormat("%v/%m")
        self.progress_bar.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.current_value))
        self.line_edit.returnPressed.connect(self.update_progress)
        self.line_edit.setContentsMargins(0, 0, 0, 0)

        self.next_button = QPushButton("+", self)
        self.next_button.clicked.connect(self.increment_value)
        self.next_button.setContentsMargins(0, 0, 0, 0)

        self.prev_button = QPushButton("-", self)
        self.prev_button.clicked.connect(self.decrement_value)
        self.prev_button.setContentsMargins(0, 0, 0, 0)

        self.progress_bar.setFixedHeight(self.line_edit.sizeHint().height())

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.progress_bar, stretch=10)
        layout.addWidget(self.prev_button, stretch=2)
        layout.addWidget(self.line_edit, stretch=3)
        layout.addWidget(self.next_button, stretch=2)

        self.setLayout(layout)

    def update_progress(self) -> None:
        """Updates the progress bar value when a new value is entered in the line edit."""

        try:
            value = int(self.line_edit.text())
            self.setValue(value)
        except ValueError:
            pass

    def setValue(self, value: int) -> None:
        """Sets the progress bar and line edit to a new value.

        Ensures the value is within the allowed range before updating.

        Args:
            value (int): The new value to set.
        """
        if 0 <= value <= self.max_value:
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.progress_bar.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self) -> None:
        """Increments the progress bar value by 1."""
        self.setValue(self.current_value + 1)

    def decrement_value(self) -> None:
        """Decrements the progress bar value by 1."""
        self.setValue(self.current_value - 1)

    def value(self) -> int:
        return self.current_value


def setup_progressbaredit(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    default: Optional[int] = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QProgressbarEdit, configure it, and add it to a layout.

    This function creates a `QProgressbarEdit` widget, sets its range and default value,
    and connects an optional callback function to the `index_changed` signal. It then
    adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QProgressbarEdit will be added.
        minimum (Optional[int], optional): The minimum value of the progress bar. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the progress bar. Defaults to None.
        default (Optional[int], optional): The initial value of the progress bar. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the progress value changes. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the progress bar. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the progress bar's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the progress bar in the layout. Defaults to 1.

    Returns:
        QWidget: The QProgressbarEdit widget added to the layout.
    """
    _widget = QProgressbarEdit(min_value=minimum, max_value=maximum, start_value=default)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
