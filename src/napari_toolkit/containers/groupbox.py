from typing import Optional, Tuple

from qtpy.QtWidgets import QBoxLayout, QGroupBox, QHBoxLayout, QLayout, QSizePolicy, QVBoxLayout


def setup_groupbox(layout: Optional[QLayout] = None, text: str = "") -> QGroupBox:
    """Create a QGroupBox and optionally add it to a given layout.

    The group box expands horizontally but has a fixed height. If a layout is provided,
    the group box is added to it.

    Args:
        layout (Optional[QLayout], optional): The layout to which the group box will be added. Defaults to None.
        text (str, optional): The title of the group box. Defaults to "".

    Returns:
        QGroupBox: The created group box.
    """
    _widget = QGroupBox(text)
    if layout is not None:
        layout.addWidget(_widget)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return _widget


def setup_hgroupbox(
    layout: Optional[QLayout] = None, text: str = ""
) -> Tuple[QGroupBox, QBoxLayout]:
    """Create a QGroupBox with a horizontal layout and optionally add it to a given layout.

    The group box contains a `QHBoxLayout` with predefined margins.

    Args:
        layout (Optional[QLayout], optional): The layout to which the group box will be added. Defaults to None.
        text (str, optional): The title of the group box. Defaults to "".

    Returns:
        Tuple[QGroupBox, QHBoxLayout]: The created group box and its horizontal layout.
    """
    _widget = setup_groupbox(layout=layout, text=text)
    _wlayout = QHBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    return _widget, _wlayout


def setup_vgroupbox(
    layout: Optional[QLayout] = None, text: str = ""
) -> Tuple[QGroupBox, QBoxLayout]:
    """Create a QGroupBox with a vertical layout and optionally add it to a given layout.

    The group box contains a `QVBoxLayout` with predefined margins.

    Args:
        layout (Optional[QLayout], optional): The layout to which the group box will be added. Defaults to None.
        text (str, optional): The title of the group box. Defaults to "".

    Returns:
        Tuple[QGroupBox, QVBoxLayout]: The created group box and its vertical layout.
    """
    _widget = setup_groupbox(layout=layout, text=text)
    _wlayout = QVBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    return _widget, _wlayout


# class MyQGroupBox(QGroupBox):
#     def __init__(self, title):
#         super().__init__(title)
#         self.setObjectName("MyQGroupBox")
#
# def setup_groupbox(layout=None, text="", v_layout=True, header=False):
#
#     _widget = QGroupBox(text)
#     if header:
#         _widget.setObjectName("Header")
#         _widget.setStyleSheet("QGroupBox#Header {color: rgb(0,100, 167);  font-size: 14px;}")
#
#     if v_layout:
#         _wlayout = QVBoxLayout()
#     else:
#         _wlayout = QHBoxLayout()
#     _widget.setLayout(_wlayout)
#     _wlayout.setContentsMargins(10, 10, 10, 10)
#     if layout is not None:
#         layout.addWidget(_widget)
#     return _widget, _wlayout
