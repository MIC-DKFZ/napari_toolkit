# flake8: noqa: E202, E231, E702
from napari.resources import get_icon_path
from PyQt5.QtWidgets import QGroupBox
from qtpy.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class QCollabsableGroupBox(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.toggled.connect(self.update)

        self.setStyleSheet(
            f"""
            QGroupBox::indicator::unchecked {{
                image: url({get_icon_path('right_arrow')});
                background: transparent;
            }}
            QGroupBox::indicator::checked {{
                image: url({get_icon_path('drop_down')});
                background: transparent;
            }}
        """
        )

    def update(self):
        for widget in self.children():
            if isinstance(widget, QWidget):
                if self.isChecked():
                    widget.show()
                else:
                    widget.hide()

    def childEvent(self, event):
        super().childEvent(event)
        self.update()


def add_collabsgroupbox(layout=None, text="", collabsed=False) -> QGroupBox:
    _widget = QCollabsableGroupBox(text)
    if layout is not None:
        layout.addWidget(_widget)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    _widget.setChecked(not collabsed)
    return _widget


def add_vcollabsgroupbox(layout=None, text="", collabsed=False) -> QGroupBox:
    _widget = add_collabsgroupbox(layout=layout, text=text, collabsed=collabsed)
    _wlayout = QVBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    return _widget, _wlayout


def add_hcollabsgroupbox(layout=None, text="", collabsed=False) -> QGroupBox:
    _widget = add_collabsgroupbox(layout=layout, text=text, collabsed=collabsed)
    _wlayout = QHBoxLayout(_widget)
    _wlayout.setContentsMargins(10, 10, 10, 10)
    return _widget, _wlayout
