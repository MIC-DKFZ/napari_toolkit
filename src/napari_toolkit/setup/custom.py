from typing import Callable, List, Optional

from napari.layers import Layer
from napari.viewer import Viewer
from qtpy.QtGui import QKeySequence
from qtpy.QtWidgets import QLayout, QShortcut, QWidget
from qtpy.QtCore import Qt
from napari_toolkit.setup.utils import connect_widget
from napari_toolkit.widgets.layer_select import QLayerSelect
from napari_toolkit.widgets.progress_edit import QProgressbarEdit
from napari_toolkit.widgets.slider_edit import QSliderEdit
from napari_toolkit.widgets.switch import QHSwitch, QVSwitch
from napari_toolkit.widgets.toggle_button import QToggleButton
from napari_toolkit.widgets.float_slider import QFloatSlider
from napari_toolkit.widgets.label_slider import QLabelSlider, QFloatLabelSlider


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


def _setup_switch(
    _widget: QWidget,
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
):
    _widget.addItems(options)

    if default is not None:
        _widget._check(default)

    if shortcut:
        key = QShortcut(QKeySequence(shortcut), _widget)
        key.activated.connect(_widget.next)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=None,
        tooltips=tooltips,
    )


def setup_vswitch(
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
):

    _widget = QVSwitch()
    return _setup_switch(_widget, layout, options, function, default, shortcut, tooltips)


def setup_hswitch(
    layout: QLayout,
    options: List[str],
    function: Optional[Callable[[str], None]] = None,
    default: int = None,
    shortcut: Optional[str] = None,
    tooltips: Optional[str] = None,
):
    _widget = QHSwitch()
    return _setup_switch(_widget, layout, options, function, default, shortcut, tooltips)


def setup_togglebutton(
    layout: QLayout,
    text: str,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QToggleButton(text)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_progressbaredit(
    layout: QLayout,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QProgressbarEdit()

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_slideredit(
    layout: QLayout,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:

    _widget = QSliderEdit()

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.index_changed,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_floatslider(
    layout: QLayout,
    digits: int = 2,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
    tick_size: Optional[int] = None,
    default: Optional[float] = None,
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

    _widget = QFloatSlider(digits=digits)
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


def setup_labelslider(
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

    _widget = QLabelSlider()

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
        widget_event=_widget.slider.sliderReleased,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_labelfloatslider(
    layout: QLayout,
    digits: int = 2,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
    tick_size: Optional[int] = None,
    default: Optional[float] = None,
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

    _widget = QFloatLabelSlider(digits=digits)

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
        widget_event=_widget.slider.sliderReleased,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
