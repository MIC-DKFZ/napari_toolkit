from napari._qt.qt_resources import QColoredSVGIcon
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QHBoxLayout, QLabel, QWidget


class QIconWrapper(QWidget):
    def __init__(
        self, widget, parent=None, icon_dict=None, color_dict=None, size=24, *args, **kwargs
    ):
        super().__init__(parent)
        # self.size = size

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self.icon_dict = icon_dict
        self.color_dict = color_dict

        self.label = QLabel()
        self.widget = widget

        self._layout.addWidget(self.label, stretch=1)
        self._layout.addWidget(self.widget, stretch=10)

        self.setLayout(self._layout)

        self.status = None
        self.set_status(None)

    def set_status(self, status):
        _icon = QColoredSVGIcon.from_resources(self.icon_dict.get(status, "none"))
        _icon = _icon.colored(color=self.color_dict.get(status, "black"))

        size = self.widget.sizeHint().height()

        _icon = _icon.pixmap(QSize(size, size), QIcon.Normal, QIcon.Off)
        self.label.setPixmap(_icon)
        self.status = status

    def __getattr__(self, name, *args, **kwargs):
        # Dynamically catch method calls and forward them
        # print(name, *args, **kwargs)
        target = getattr(self.widget, name)  # target = getattr(self.forward_to, name)
        if callable(target):

            def wrapper(*args, **kwargs):
                print(f"MyClass: Forwarding call to {name} with args={args}, kwargs={kwargs}")
                return target(*args, **kwargs)

            return wrapper
        return target

    def __setattr__(self, name, value):
        try:
            return super().__setattr__(name, value)
        except AttributeError:
            return setattr(self.widget, name, value)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return getattr(self.widget, name)

    def __delattr__(self, name):
        try:
            return super().__delattr__(name)
        except AttributeError:
            return delattr(self.widget, name)
