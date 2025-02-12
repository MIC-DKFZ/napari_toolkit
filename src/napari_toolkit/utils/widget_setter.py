from typing import Any

from qtpy.QtCore import QDateTime
from qtpy.QtWidgets import (
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
    QWidget,
)

from napari_toolkit.widgets.buttons.toggle_button import QToggleButton
from napari_toolkit.widgets.color.color_picker import QColorPicker
from napari_toolkit.widgets.color.edit_color_picker import QEditColorPicker
from napari_toolkit.widgets.file_select import QDirSelect, QFileSelect
from napari_toolkit.widgets.progressbar.progress_edit import QProgressbarEdit
from napari_toolkit.widgets.sliders.double_slider import QDoubleSlider
from napari_toolkit.widgets.sliders.edit_slider import QEditDoubleSlider, QEditSlider
from napari_toolkit.widgets.sliders.labeled_slider import QLabeledDoubleSlider, QLabeledSlider
from napari_toolkit.widgets.switch import QHSwitch, QVSwitch


def set_value(widget: QWidget, value: Any) -> None:
    """Retrieves the value from a given QWidget based on its type.

    Args:
        widget (QWidget): The widget to extract the value from.
        value (Any): The value to be assigned to the widget

    Raises:
        TypeError: If the widget type is unsupported.
        ValueError: If the provided value is of an invalid type.
    """
    # 1. Buttons & Checkable Widgets
    if isinstance(widget, (QCheckBox, QRadioButton, QToggleButton)):
        if not isinstance(value, bool):
            raise ValueError(f"Expected a boolean for {type(widget).__name__}, got {type(value)}.")
        widget.setChecked(value)
    # 2. Input & Text Fields
    elif isinstance(widget, QLineEdit):
        if not isinstance(value, str):
            raise ValueError(f"Expected a string for {type(widget).__name__}, got {type(value)}.")
        widget.setText(value)
    elif isinstance(widget, (QTextEdit, QPlainTextEdit)):
        if not isinstance(value, str):
            raise ValueError(f"Expected a string for {type(widget).__name__}, got {type(value)}.")
        widget.setPlainText(value)
    # 3. Numeric Inputs (Spinbox, Slider, Progress)
    elif isinstance(
        widget,
        (
            QSpinBox,
            QDoubleSpinBox,
            QSlider,
            QDoubleSlider,
            QLabeledSlider,
            QLabeledDoubleSlider,
            QEditSlider,
            QEditDoubleSlider,
            QProgressBar,
            QProgressbarEdit,
        ),
    ):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Expected a number for {type(widget).__name__}, got {type(value)}.")
        widget.setValue(value)
    # 4. Selection Widgets
    elif isinstance(widget, (QComboBox, QVSwitch, QHSwitch)):
        if isinstance(value, str):
            index = widget.findText(value)
            if index != -1:
                widget.setCurrentIndex(index)
        elif isinstance(value, int):
            widget.setCurrentIndex(value)
    # 5.1 Dialog - Date
    elif isinstance(widget, QDateTimeEdit):
        if isinstance(value, str):
            # print("Z",QDateTime.fromString(value).dateTime())
            widget.setDateTime(QDateTime.fromString(value, "yyyy-MM-dd HH:mm:ss"))
        else:
            raise ValueError(f"Expected a string for QDateTimeEdit, got {type(value)}.")
    # 5.2 Dialog - Color
    elif isinstance(widget, (QColorPicker, QEditColorPicker)):
        widget.set_color(value)  # Set as (R, G, B)

    # 5.3 Dialog - File
    elif isinstance(widget, QFileSelect):
        widget.set_file(value)
    elif isinstance(widget, QDirSelect):
        widget.set_dir(value)
    # Unsuported
    else:
        raise TypeError(f"Unsupported widget type: {type(widget).__name__}")
