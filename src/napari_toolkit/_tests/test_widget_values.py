import pytest
from qtpy.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDoubleSpinBox,
    QLineEdit,
    QPlainTextEdit,
    QProgressBar,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTextEdit,
)

from napari_toolkit.utils.widget_getter import get_value
from napari_toolkit.utils.widget_setter import set_value
from napari_toolkit.widgets.buttons.toggle_button import QToggleButton
from napari_toolkit.widgets.color.color_picker import QColorPicker
from napari_toolkit.widgets.color.edit_color_picker import QEditColorPicker
from napari_toolkit.widgets.file_select import QDirSelect, QFileSelect
from napari_toolkit.widgets.progressbar.progress_edit import QProgressbarEdit
from napari_toolkit.widgets.sliders.double_slider import QDoubleSlider
from napari_toolkit.widgets.sliders.edit_slider import QEditDoubleSlider, QEditSlider
from napari_toolkit.widgets.sliders.labeled_slider import QLabeledDoubleSlider, QLabeledSlider
from napari_toolkit.widgets.switch import QHSwitch, QVSwitch

# Required for PyQt/PySide testing
app = QApplication([])


@pytest.mark.parametrize(
    "widget_cls, value",
    [
        # Checkable Widgets
        (QCheckBox, True),
        (QRadioButton, False),
        (QToggleButton, True),
        # Text Input Widgets
        (QLineEdit, "Hello, Napari!"),
        (QTextEdit, "Multi-line text"),
        (QPlainTextEdit, "Another text field"),
        # Numeric Input Widgets
        (QSpinBox, 42),
        (QDoubleSpinBox, 3.14),
        (QSlider, 75),
        (QDoubleSlider, 2.7),
        (QLabeledSlider, 50),
        (QLabeledDoubleSlider, 1.2),
        (QEditSlider, 99),
        (QEditDoubleSlider, 0.1),
        (QProgressBar, 80),
        (QProgressbarEdit, 60),
        # Selection Widgets
        (QComboBox, "Green"),
        (QVSwitch, "Green"),
        (QHSwitch, "Green"),
        (QComboBox, 1),
        (QVSwitch, 1),
        (QHSwitch, 1),
        # Date & Time
        (QDateTimeEdit, "2025-02-10 14:30:00"),
        # File & Directory Selectors
        (QFileSelect, "/home/user/file.txt"),
        (QDirSelect, "/home/user/documents"),
        # Color Picker
        (QColorPicker, (255, 0, 0)),
        (QEditColorPicker, (0, 255, 255, 0.5)),
    ],
)
def test_widget_set_get(widget_cls, value):
    """Tests the setter and getter methods for all supported widgets."""

    widget = widget_cls()

    # Special handling for QComboBox (it requires predefined items)
    if isinstance(widget, (QComboBox, QHSwitch, QVSwitch)):
        widget.addItems(["Red", "Green", "Blue"])

    # Apply the setter function
    set_value(widget, value)

    # Retrieve the value using the getter function
    retrieved_value = get_value(widget)

    # Special handling for QColorPicker (returns tuple, needs conversion)
    if isinstance(widget, (QColorPicker, QEditColorPicker)) and isinstance(value, tuple):
        assert tuple(retrieved_value) == value
    elif isinstance(widget, (QComboBox, QHSwitch, QVSwitch)):
        if isinstance(value, str):
            assert retrieved_value[0] == value
        else:
            assert retrieved_value[1] == value
    else:
        assert (
            retrieved_value == value
        ), f"Mismatch for {widget_cls.__name__}: Expected {value}, got {retrieved_value}"
