from typing import Callable, Optional, Tuple

from qtpy.QtCore import QDateTime
from qtpy.QtWidgets import QDateTimeEdit, QLayout, QWidget

from napari_toolkit.setup.utils import connect_widget
from napari_toolkit.widgets.color_picker import QColorPicker
from napari_toolkit.widgets.file_select import QDirSelect, QFileSelect


def setup_colorpicker(
    layout: QLayout,
    initial_color: Tuple[int] = (255, 255, 255),
    size: int = 30,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QColorPicker(initial_color, size)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_fileselect(
    layout: QLayout,
    text: str = "Select",
    read_only: bool = True,
    default_dir: str = None,
    filter: str = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QFileSelect(
        text=text,
        filter=filter,
        read_only=read_only,
        default_dir=default_dir,
        save_file=False,
    )

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.button.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_savefileselect(
    layout: QLayout,
    text: str = "Select",
    read_only: bool = True,
    default_dir: str = None,
    filter: str = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QFileSelect(
        text=text,
        filter=filter,
        read_only=read_only,
        default_dir=default_dir,
        save_file=True,
    )

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.button.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_dirselect(
    layout: QLayout,
    text: str = "Select",
    read_only: bool = True,
    default_dir: str = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QDirSelect(text=text, read_only=read_only, default_dir=default_dir)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.button.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_timeedit(
    layout: QLayout,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    _widget = QDateTimeEdit()
    _widget.setDateTime(QDateTime.currentDateTime())

    return connect_widget(
        layout,
        _widget,
        widget_event=None,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
