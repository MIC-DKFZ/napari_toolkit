from typing import Callable, Optional

from qtpy.QtWidgets import (
    QLabel,
    QLayout,
    QLineEdit,
    QPlainTextEdit,
    QSizePolicy,
    QTextEdit,
    QWidget,
)

from napari_toolkit.utils.utils import connect_widget


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
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.textChanged,
        function=function,
        shortcut=None,
        tooltips=tooltips,
        stretch=stretch,
    )
