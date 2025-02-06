from qtpy.QtCore import Signal
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class _QSwitch(QWidget):
    """A widget that provides a toggleable switch with multiple button options."""

    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.buttons = []
        self.options = []
        self.value = None
        self.index = None
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)

    def addItems(self, items):
        """Add Items as buttons to the widget"""
        for i, item in enumerate(items):
            _btn = QPushButton(item)
            _btn.clicked.connect(lambda _, idx=i: self._on_button_pressed(idx))
            self._layout.addWidget(_btn)
            self.buttons.append(_btn)
            self.options.append(item)

    def _on_button_pressed(self, idx: int):
        """
        Handles the button press event, updating the selected option.

        Args:
            idx (int): Index of the button pressed.
        """
        self._uncheck()
        self._check(idx)
        self.clicked.emit()

    def _uncheck(self):
        """Unchecks all buttons and resets the selection state."""
        self.value = None
        self.index = None
        for btn in self.buttons:
            btn.setChecked(False)
            btn.setStyleSheet("")

    def _check(self, idx: int):
        """
        Checks the button at the specified index and updates the selection state.

        Args:
            idx (int): Index of the button to check.
        """
        if idx is not None and 0 <= idx < len(self.buttons):
            self.value = self.options[idx]
            self.index = idx
            self.buttons[idx].setChecked(True)
            self.buttons[idx].setStyleSheet("QPushButton {background-color: rgb(0,100, 167);}")

    def next(self, *args, **kwargs):
        """Just go to the next item"""
        idx = (self.index + 1) % len(self.options)
        self._on_button_pressed(idx)


class QHSwitch(_QSwitch):
    """
    A horizontal switch widget with multiple button options.

    Args:
        options (List[str]): List of option names for each button.
        function (Callable[[], None]): Function to call when a button is pressed.
        default (Optional[int], optional): Index of the default selected option. Defaults to None.
        shortcuts (Optional[List[str]], optional): List of keyboard shortcuts for each option. Defaults to None.
    """

    def __init__(self, parent=None):
        self._layout = QHBoxLayout()
        super().__init__(parent)


class QVSwitch(_QSwitch):
    """
    A vertical switch widget with multiple button options.

    Args:
        options (List[str]): List of option names for each button.
        function (Callable[[], None]): Function to call when a button is pressed.
        default (Optional[int], optional): Index of the default selected option. Defaults to None.
        shortcuts (Optional[List[str]], optional): List of keyboard shortcuts for each option. Defaults to None.
    """

    def __init__(self, parent=None):
        self._layout = QVBoxLayout()
        super().__init__(parent)
