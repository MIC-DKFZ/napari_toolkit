from qtpy.QtWidgets import QHBoxLayout, QVBoxLayout


def stack(boxlayout, widgets, stretch=None):
    stretch = stretch if stretch is not None else [1] * len(widgets)
    for _widget, s in zip(widgets, stretch):
        boxlayout.addWidget(_widget, stretch=s)
    return boxlayout


def hstack(layout, widgets, stretch=None):
    _boxlayout = QHBoxLayout()
    layout.addLayout(_boxlayout)
    return stack(_boxlayout, widgets, stretch)


def vstack(layout, widgets, stretch=None):
    _boxlayout = QVBoxLayout()
    layout.addLayout(_boxlayout)
    return stack(_boxlayout, widgets, stretch)
