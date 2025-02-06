from typing import Any, Callable, List, Optional

from PyQt5.QtWidgets import QTableWidgetItem
from qtpy.QtCore import Qt
from qtpy.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLayout,
    QLineEdit,
    QListWidget,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTableWidget,
    QTextEdit,
    QTreeWidget,
    QWidget,
)

from napari_toolkit.setup.utils import connect_widget


def setup_button(
    layout: QLayout,
    text: str,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QPushButton, configure it, and add it to a layout.

    This function creates a QPushButton with the specified text, connects it
    to an optional callback function, sets tooltips and shortcuts if provided,
    and adds it to the given layout with the specified stretch factor.

    Args:
        layout (QLayout): The layout to which the button will be added.
        text (str): The text to display on the button.
        function (Optional[Callable], optional): The function to connect to the button's `clicked` event.
            Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the button.
            Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the button. Defaults to None.
        stretch (int, optional): The stretch factor for the button in the layout. Defaults to 1.

    Returns:
        QWidget: The QPushButton widget added to the layout.
    """

    _widget = QPushButton(text)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_slider(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    tick_size: Optional[int] = None,
    default: Optional[int] = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QSlider, configure it, and add it to a layout.

    This function creates a horizontal `QSlider`, configures its range, tick size,
    and default value if provided. It connects an optional callback function to the
    slider's `sliderReleased` event and adds the slider to the specified layout.

    Args:
        layout (QLayout): The layout to which the slider will be added.
        minimum (Optional[int], optional): The minimum value of the slider. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the slider. Defaults to None.
        tick_size (Optional[int], optional): The interval between slider ticks. Defaults to None.
        default (Optional[int], optional): The initial value of the slider. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute on slider release. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the slider. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the slider's associated action. Defaults to None.
        stretch (int, optional): The stretch factor for the slider in the layout. Defaults to 1.

    Returns:
        QWidget: The QSlider widget added to the layout.
    """

    _widget = QSlider()
    _widget.setOrientation(Qt.Horizontal)

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default is not None:
        _widget.setValue(default)
    if tick_size is not None:
        _widget.setTickInterval(tick_size)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.sliderReleased,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_spinbox(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    step_size: Optional[int] = None,
    default: Optional[int] = None,
    function: Optional[Callable] = None,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QSpinBox, configure it, and add it to a layout.

    This function creates a `QSpinBox`, configures its range, step size,
    prefix, suffix, and default value if provided. It connects an optional
    callback function to the spinbox's `valueChanged` event and adds it
    to the specified layout.

    Args:
        layout (QLayout): The layout to which the spinbox will be added.
        minimum (Optional[int], optional): The minimum value of the spinbox. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the spinbox. Defaults to None.
        step_size (Optional[int], optional): The step size for incrementing/decrementing the value. Defaults to None.
        default (Optional[int], optional): The initial value of the spinbox. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the value changes. Defaults to None.
        prefix (Optional[str], optional): Text to display before the spinbox value. Defaults to None.
        suffix (Optional[str], optional): Text to display after the spinbox value. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the spinbox. Defaults to None.
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.

    Returns:
        QWidget: The QSpinBox widget added to the layout.
    """
    _widget = QSpinBox()

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default:
        _widget.setValue(default)
    if step_size is not None:
        _widget.setSingleStep(step_size)
    if suffix is not None:
        _widget.setSuffix(suffix)
    if prefix is not None:
        _widget.setPrefix(prefix)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.valueChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_doublespinbox(
    layout: QLayout,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
    step_size: Optional[float] = None,
    default: Optional[float] = None,
    function: Optional[Callable] = None,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    digits: int = 2,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QDoubleSpinBox, configure it, and add it to a layout.

    This function creates a `QDoubleSpinBox`, configures its range, step size,
    prefix, suffix, number of decimals, and default value if provided. It connects
    an optional callback function to the spinbox's `valueChanged` event and adds
    it to the specified layout.

    Args:
        layout (QLayout): The layout to which the spinbox will be added.
        minimum (Optional[float], optional): The minimum value of the spinbox. Defaults to None.
        maximum (Optional[float], optional): The maximum value of the spinbox. Defaults to None.
        step_size (Optional[float], optional): The step size for incrementing/decrementing the value. Defaults to None.
        default (Optional[float], optional): The initial value of the spinbox. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the value changes. Defaults to None.
        prefix (Optional[str], optional): Text to display before the spinbox value. Defaults to None.
        suffix (Optional[str], optional): Text to display after the spinbox value. Defaults to None.
        digits (int, optional): The number of decimal places to display. Defaults to 2.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the spinbox. Defaults to None.
        stretch (int, optional): The stretch factor for the spinbox in the layout. Defaults to 1.

    Returns:
        QWidget: The QDoubleSpinBox widget added to the layout.
    """
    _widget = QDoubleSpinBox()
    _widget.setDecimals(digits)

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default:
        _widget.setValue(default)
    if step_size is not None:
        _widget.setSingleStep(step_size)
    if suffix is not None:
        _widget.setSuffix(suffix)
    if prefix is not None:
        _widget.setPrefix(prefix)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.valueChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_label(
    layout: QLayout,
    text: str,
    verbose: bool = False,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QLabel, configure it, and add it to a layout.

    This function creates a `QLabel` with the specified text, enables word wrapping,
    and optionally displays the text in the console if verbose mode is enabled.
    It also adds the label to the specified layout.

    Args:
        layout (QLayout): The layout to which the label will be added.
        text (str): The text to display in the label.
        verbose (bool, optional): If True, prints the text to the console. Defaults to False.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the label. Defaults to None.
        stretch (int, optional): The stretch factor for the label in the layout. Defaults to 1.

    Returns:
        QWidget: The QLabel widget added to the layout.
    """
    _widget = QLabel(text)
    _widget.setWordWrap(True)

    if verbose:
        print(text)

    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=None,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_lineedit(
    layout: QLayout,
    text: Optional[str] = None,
    placeholder: Optional[str] = None,
    function: Optional[Callable] = None,
    readonly: bool = False,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QLineEdit, configure it, and add it to a layout.

    This function creates a `QLineEdit` widget, sets its text, placeholder,
    and read-only status if provided. It connects an optional callback function
    to the `returnPressed` signal and adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QLineEdit will be added.
        text (Optional[str], optional): The initial text to display in the QLineEdit. Defaults to None.
        placeholder (Optional[str], optional): Placeholder text for the QLineEdit. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the `returnPressed` signal is triggered. Defaults to None.
        readonly (bool, optional): If True, makes the QLineEdit read-only. Defaults to False.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the QLineEdit. Defaults to None.
        stretch (int, optional): The stretch factor for the QLineEdit in the layout. Defaults to 1.

    Returns:
        QWidget: The QLineEdit widget added to the layout.
    """
    _widget = QLineEdit()
    _widget.setReadOnly(readonly)
    if text is not None:
        _widget.setText(text)
    if placeholder is not None:
        _widget.setPlaceholderText(placeholder)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.returnPressed,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_textedit(
    layout: QLayout,
    text: Optional[str] = None,
    placeholder: Optional[str] = None,
    function: Optional[Callable] = None,
    readonly: bool = False,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QTextEdit, configure it, and add it to a layout.

    This function creates a `QTextEdit` widget, sets its text, placeholder,
    and read-only status if provided. It connects an optional callback function
    to the `textChanged` signal and adds the widget to the specified layout.

    Args:
        layout (QLayout): The layout to which the QTextEdit will be added.
        text (Optional[str], optional): The initial text to display in the QTextEdit. Defaults to None.
        placeholder (Optional[str], optional): Placeholder text for the QTextEdit. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the `textChanged` signal is triggered. Defaults to None.
        readonly (bool, optional): If True, makes the QTextEdit read-only. Defaults to False.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the QTextEdit. Defaults to None.
        stretch (int, optional): The stretch factor for the QTextEdit in the layout. Defaults to 1.

    Returns:
        QWidget: The QTextEdit widget added to the layout.
    """
    _widget = QTextEdit()
    _widget.setReadOnly(readonly)
    if text is not None:
        _widget.setText(text)
    if placeholder is not None:
        _widget.setPlaceholderText(placeholder)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.textChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_plaintextedit(
    layout: QLayout,
    text: Optional[str] = None,
    placeholder: Optional[str] = None,
    function: Optional[Callable] = None,
    readonly: bool = False,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QPlainTextEdit, configure it, and add it to a layout.

    This function creates a `QPlainTextEdit` widget, sets its plain text,
    placeholder, and read-only status if provided. It connects an optional
    callback function to the `textChanged` signal and adds the widget to the
    specified layout.

    Args:
        layout (QLayout): The layout to which the QPlainTextEdit will be added.
        text (Optional[str], optional): The initial plain text to display in the QPlainTextEdit. Defaults to None.
        placeholder (Optional[str], optional): Placeholder text for the QPlainTextEdit. Defaults to None.
        function (Optional[Callable], optional): A callback function to execute when the `textChanged` signal is triggered. Defaults to None.
        readonly (bool, optional): If True, makes the QPlainTextEdit read-only. Defaults to False.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the QPlainTextEdit. Defaults to None.
        stretch (int, optional): The stretch factor for the QPlainTextEdit in the layout. Defaults to 1.

    Returns:
        QWidget: The QPlainTextEdit widget added to the layout.
    """
    _widget = QPlainTextEdit()
    _widget.setReadOnly(readonly)
    if text is not None:
        _widget.setPlainText(text)
    if placeholder is not None:
        _widget.setPlaceholderText(placeholder)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.textChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


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

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.currentTextChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_checkbox(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QCheckBox, configure it, and add it to a layout.

    This function creates a `QCheckBox` widget, sets its initial checked state,
    and connects an optional callback function to the `stateChanged` signal.
    It then adds the checkbox to the specified layout.

    Args:
        layout (QLayout): The layout to which the QCheckBox will be added.
        text (str): The text label for the checkbox.
        checked (bool): The initial checked state of the checkbox. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the `stateChanged` signal is triggered. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the checkbox. Defaults to None.
        stretch (int, optional): The stretch factor for the checkbox in the layout. Defaults to 1.

    Returns:
        QWidget: The QCheckBox widget added to the layout.
    """
    _widget = QCheckBox(text)
    _widget.setChecked(checked)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.stateChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_radiobutton(
    layout: QLayout,
    text: str,
    checked: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QRadioButton, configure it, and add it to a layout.

    This function creates a `QRadioButton` widget, sets its initial checked state,
    and connects an optional callback function to the `toggled` signal.
    It then adds the radio button to the specified layout.

    Args:
        layout (QLayout): The layout to which the QRadioButton will be added.
        text (str): The text label for the radio button.
        checked (bool): The initial checked state of the radio button. Defaults to False.
        function (Optional[Callable], optional): A callback function to execute when the `toggled` signal is triggered. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the radio button. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the radio button. Defaults to None.
        stretch (int, optional): The stretch factor for the radio button in the layout. Defaults to 1.

    Returns:
        QWidget: The QRadioButton widget added to the layout.
    """

    _widget = QRadioButton(text)
    _widget.setChecked(checked)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.toggled,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_progressbar(
    layout: QLayout,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
    default: Optional[int] = None,
    percentage: bool = False,
    tooltips: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Create a QProgressBar, configure it, and add it to a layout.

    This function creates a `QProgressBar` widget, sets its range, default value,
    and whether or not to display the percentage text. It adds the widget to the
    specified layout.

    Args:
        layout (QLayout): The layout to which the QProgressBar will be added.
        minimum (Optional[int], optional): The minimum value of the progress bar. Defaults to None.
        maximum (Optional[int], optional): The maximum value of the progress bar. Defaults to None.
        default (Optional[int], optional): The initial value of the progress bar. Defaults to None.
        percentage (bool, optional): If True, shows percentage text on the progress bar. Defaults to False.
        tooltips (Optional[str], optional): Tooltip text to display when hovering over the progress bar. Defaults to None.
        stretch (int, optional): The stretch factor for the progress bar in the layout. Defaults to 1.

    Returns:
        QWidget: The QProgressBar widget added to the layout.
    """
    _widget = QProgressBar()
    _widget.setTextVisible(percentage)

    if minimum is not None:
        _widget.setMinimum(minimum)
    if maximum is not None:
        _widget.setMaximum(maximum)
    if default:
        _widget.setValue(default)

    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=None,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_list(
    layout: QLayout,
    options: List[str],
    multiple: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QListWidget()
    _widget.addItems(options)
    if multiple:
        _widget.setSelectionMode(QAbstractItemView.MultiSelection)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.itemClicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_tree(
    layout: QLayout,
    header: Optional[List[str]] = None,
    multiple: bool = False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """
    from qtpy.QtWidgets import QTreeWidgetItem
    t1 = QTreeWidgetItem(_widget, ["Parent Item", "10"])
    c1 = QTreeWidgetItem(t1, ["Child 1", "20"])
    c2 = QTreeWidgetItem(t1, ["Child 2", "30"])
    """

    _widget = QTreeWidget()
    if header is not None:
        _widget.setHeaderLabels(header)
    if multiple:
        _widget.setSelectionMode(QAbstractItemView.MultiSelection)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.itemClicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_table(
    layout: QLayout,
    data: List[List[Any]],
    header: Optional[List[str]] = None,
    show_index=True,
    editable=False,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """
    # Populate the table with data
    table.setItem(0, 0, QTableWidgetItem("Row 1, Col 1"))
    table.setItem(0, 1, QTableWidgetItem("Row 1, Col 2"))
    table.setItem(1, 0, QTableWidgetItem("Row 2, Col 1"))
    table.setItem(1, 1, QTableWidgetItem("Row 2, Col 2"))
    """

    _widget = QTableWidget()
    if header is not None:
        _widget.setColumnCount(len(header))
        _widget.setHorizontalHeaderLabels(header)

    if data is not None:
        _widget.setRowCount(len(data))
        for i, di in enumerate(data):
            for j, dj in enumerate(di):
                _widget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
    _widget.resizeColumnsToContents()
    if not editable:
        _widget.setEditTriggers(QTableWidget.NoEditTriggers)
    _widget.verticalHeader().setVisible(show_index)

    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
