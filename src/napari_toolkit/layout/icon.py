from napari_toolkit.widgets.icon_wrapper import QIconWrapper


def add_icon(layout, widget, icon_dict=None, color_dict=None, size=24):
    _widget = QIconWrapper(widget, icon_dict=icon_dict, color_dict=color_dict, size=size)
    layout.addWidget(_widget)
    return _widget
