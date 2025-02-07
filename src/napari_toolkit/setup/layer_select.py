from typing import Callable, Optional

from napari.layers import Layer
from napari.viewer import Viewer
from qtpy.QtWidgets import QLayout, QWidget

from napari_toolkit.setup.utils import connect_widget
from napari_toolkit.widgets.layer_select import QLayerSelect


def setup_layerselect(
    layout: QLayout,
    viewer: Optional[Viewer] = None,
    layer_type: Optional[Layer] = Layer,
    function: Optional[Callable[[str], None]] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
) -> QWidget:
    """
    Adds a LayerSelectionWidget to a layout with optional configurations, including connecting
    a function, setting a tooltip, and adding a keyboard shortcut.

    Args:
        layout (QLayout): The layout to add the LayerSelectionWidget to.
        viewer (Optional[Viewer], optional): The Napari viewer instance to connect the widget to. Defaults to None.
        layer_type (Optional[Type[Layer]], optional): A specific Napari layer type to filter by in the selection widget.
        function (Optional[Callable[[str], None]], optional): The function to call when the selection changes.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut to trigger the function. Defaults to None.

    Returns:
        QWidget: The configured LayerSelectionWidget added to the layout.
    """
    _widget = QLayerSelect(layer_type=layer_type)
    if viewer:
        _widget.connect(viewer)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.currentTextChanged,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
    )
