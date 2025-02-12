from typing import Any

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


def get_value(widget: QWidget) -> Any:
    """Retrieves the value from a given QWidget based on its type.

    Args:
        widget (QWidget): The widget to extract the value from.

    Returns:
        Any: The value of the widget, depending on its type.

    Raises:
        TypeError: If the widget type is unsupported.
    """
    # 1. Buttons & Checkable Widgets
    if isinstance(widget, (QCheckBox, QRadioButton, QToggleButton)):
        return widget.isChecked()
    # 2. Input & Text Fields
    elif isinstance(widget, QLineEdit):
        return widget.text()
    elif isinstance(widget, (QTextEdit, QPlainTextEdit)):
        return widget.toPlainText()
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
        return widget.value()
    # 4. Selection Widgets
    elif isinstance(widget, (QComboBox, QVSwitch, QHSwitch)):
        return widget.currentText(), widget.currentIndex()
    # 5.1 Dialog - Date
    elif isinstance(widget, QDateTimeEdit):
        return widget.dateTime().toString("yyyy-MM-dd HH:mm:ss")
    # 5.2 Dialog - Color
    elif isinstance(widget, (QColorPicker, QEditColorPicker)):
        return widget.get_color()
    # 5.3 Dialog - File
    elif isinstance(widget, QFileSelect):
        return widget.get_file()
    elif isinstance(widget, QDirSelect):
        return widget.get_dir()

    # Unsuported
    raise TypeError(f"Unsupported widget type: {type(widget).__name__}")
