from qtpy.QtWidgets import QGroupBox, QHBoxLayout, QSizePolicy, QVBoxLayout


def add_groupbox(layout=None, text="") -> QGroupBox:
    _widget = QGroupBox(text)
    if layout is not None:
        layout.addWidget(_widget)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return _widget


def add_hgroupbox(layout=None, text="") -> QGroupBox:
    _widget = add_groupbox(layout=layout, text=text)
    _wlayout = QHBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    return _widget, _wlayout


def add_vgroupbox(layout=None, text="") -> QGroupBox:
    _widget = add_groupbox(layout=layout, text=text)
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
