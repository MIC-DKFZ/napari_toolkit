from typing import Optional

import napari
from napari.layers import Image, Labels
from napari.viewer import Viewer
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QTreeWidgetItem, QVBoxLayout, QWidget

from napari_toolkit.containers import (
    setup_hgroupbox,
    setup_scrollarea,
    setup_tabwidget,
    setup_vcollapsiblegroupbox,
)
from napari_toolkit.data_structs import setup_list, setup_table, setup_tree
from napari_toolkit.widgets import (
    setup_acknowledgements,
    setup_checkbox,
    setup_colorbar,
    setup_colorpicker,
    setup_combobox,
    setup_dirselect,
    setup_doubleslider,
    setup_doublespinbox,
    setup_editcolorpicker,
    setup_editdoubleslider,
    setup_editslider,
    setup_fileselect,
    setup_hswitch,
    setup_icon_wrapper,
    setup_iconbutton,
    setup_label,
    setup_labeleddoubleslider,
    setup_labeledslider,
    setup_layerselect,
    setup_lineedit,
    setup_plaintextedit,
    setup_progressbar,
    setup_progressbaredit,
    setup_pushbutton,
    setup_radiobutton,
    setup_savefileselect,
    setup_slider,
    setup_spinbox,
    setup_textedit,
    setup_timeedit,
    setup_togglebutton,
    setup_vswitch,
)


class GalleryWidget(QWidget):
    """A widget that displays multiple gallery pages within a Napari viewer.

    This widget organizes multiple pages within a horizontal layout and integrates
    with a Napari viewer instance.

    Attributes:
        _viewer (Viewer): The Napari viewer instance.
    """

    def __init__(self, viewer: Viewer, parent: Optional[QWidget] = None):
        """Initializes the GalleryWidget with multiple pages.

        Args:
            viewer (Viewer): The Napari viewer instance.
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self._viewer = viewer
        _main_layout = QHBoxLayout(self)

        _main_layout.addWidget(self.init_page1())
        _main_layout.addWidget(self.init_page2())
        _main_layout.addWidget(self.init_page3())
        _main_layout.addWidget(self.init_page4())

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # change_theme(self._viewer)

    def init_page1(self):
        """Initializes and returns the first gallery page.

        Returns:
            QWidget: The first gallery page widget.
        """
        _container = QWidget()
        _layout = QVBoxLayout(_container)
        _container.setMinimumWidth(230)
        _container.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        _layout.setAlignment(Qt.AlignTop)

        # GROUPBOX
        _, _ = setup_hgroupbox(_layout, "QGroupBox")
        _, _ = setup_vcollapsiblegroupbox(_layout, "QCollapsibleGroupBox", False)
        _, _ = setup_vcollapsiblegroupbox(_layout, "QCollapsibleGroupBox", True)

        # SCROLLAREA
        groub_scr, layout_scr = setup_vcollapsiblegroupbox(_layout, "QScrollArea", False)
        label = QLabel("This is a long text.\n" * 20)
        label.setFixedWidth(200)

        _ = setup_scrollarea(layout_scr, widgets=label, max_height=200)

        # TABWIDGET
        groub_tab, layout_tab = setup_vcollapsiblegroupbox(_layout, "QTabWidget", False)
        tab1 = QLabel("Page1.\n" * 10)
        tab2 = QLabel("Page2.\n" * 5)
        _ = setup_tabwidget(layout_tab, [tab1, tab2], ["Page1", "Page2"])

        # Text Edit
        groub_tx, layout_tx = setup_vcollapsiblegroupbox(_layout, "Text Edit", False)
        _ = setup_label(layout_tx, "QLabel")
        _ = setup_lineedit(layout_tx, "QLineEdit", "QLineEdit", function=lambda: print("QLineEdit"))
        _ = setup_textedit(layout_tx, "QTextEdit", "QTextEdit", function=lambda: print("QTextEdit"))
        _ = setup_plaintextedit(
            layout_tx, "QPlainTextEdit", "QPlainTextEdit", function=lambda: print("QPlainTextEdit")
        )

        return _container

    def init_page2(self):
        """Initializes and returns the second gallery page.

        Returns:
            QWidget: The second gallery page widget.
        """
        _container = QWidget()
        _layout = QVBoxLayout(_container)
        _container.setMinimumWidth(230)
        _container.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        _layout.setAlignment(Qt.AlignTop)

        # Combobox
        groub_cb, layout_cb = setup_vcollapsiblegroupbox(_layout, "QComboBox", False)
        _ = setup_combobox(
            layout_cb, ["A", "B", "C"], "QComboBox", function=lambda: print("QComboBox")
        )

        # Checkbox
        groub_ch, layout_ch = setup_vcollapsiblegroupbox(_layout, "QCheckBox", False)
        _ = setup_checkbox(layout_ch, "QCheckBox", function=lambda: print("QCheckBox"))

        # BUTTONS
        groub_btn, layout_btn = setup_vcollapsiblegroupbox(_layout, "Buttons", False)
        _ = setup_pushbutton(layout_btn, "QPushButton", function=lambda: print("QPushButton"))
        layout_rbtn = QHBoxLayout()
        layout_btn.addLayout(layout_rbtn)
        _ = setup_radiobutton(
            layout_rbtn, "QRadioButton", False, function=lambda: print("QRadioButton")
        )
        _ = setup_radiobutton(
            layout_rbtn, "QRadioButton", True, function=lambda: print("QRadioButton_2")
        )
        layout_tbtn = QHBoxLayout()
        layout_btn.addLayout(layout_tbtn)
        _ = setup_togglebutton(
            layout_tbtn, "QToggleButton", function=lambda: print("QToggleButton")
        )
        _ = setup_togglebutton(
            layout_tbtn, "QToggleButton", True, function=lambda: print("QToggleButton_2")
        )
        _ = setup_iconbutton(
            layout_btn,
            "QIconButton",
            "rectangle",
            theme=self._viewer.theme,
            function=lambda: print("QIconButton"),
        )
        _ = setup_iconbutton(
            layout_btn,
            "QIconButton",
            "delete",
            theme=self._viewer.theme,
            function=lambda: print("QIconButton"),
        )

        # SPINBOX
        groub_sb, layout_sb = setup_vcollapsiblegroupbox(_layout, "SpinBox", False)
        _ = setup_label(layout_sb, "QSpinBox")
        _ = setup_spinbox(layout_sb, 0, 25, 1, 5, function=lambda: print("QSpinBox"))
        _ = setup_label(layout_sb, "QDoubleSpinBox")
        _ = setup_doublespinbox(
            layout_sb, 0, 25.5, 0.05, 2, function=lambda: print("DoubleSpinbox"), digits=3
        )

        # Slider
        groub_sl, layout_sl = setup_vcollapsiblegroupbox(_layout, "Slider", False)
        _ = setup_label(layout_sl, "QSlider")
        _ = setup_slider(layout_sl, 0, 50, 10, 30, function=lambda: print("QSlider"))
        _ = setup_label(layout_sl, "QLabeledSlider")
        _ = setup_labeledslider(layout_sl, 0, 50, 5, 30, function=lambda: print("QLabeledSlider"))
        _ = setup_label(layout_sl, "QEditSlider")
        _ = setup_editslider(layout_sl, function=lambda: print("QEditSlider"))
        _ = setup_editslider(
            layout_sl, function=lambda: print("QEditSlider"), include_buttons=False
        )
        # DoubleSlider
        _ = setup_label(layout_sl, "QDoubleSlider")
        _ = setup_doubleslider(
            layout_sl, 2, 0, 2.3, 0.5, 1.5, function=lambda: print("QDoubleSlider")
        )
        _ = setup_label(layout_sl, "QLabeledDoubleSlider")
        _ = setup_labeleddoubleslider(
            layout_sl, 2, 0, 2.3, 1, 1.0, function=lambda: print("QLabeledDoubleSlider")
        )
        _ = setup_label(layout_sl, "QEditSlider")
        _ = setup_editdoubleslider(layout_sl, 2, 0, 2.3, 1.1, function=lambda: print("QEditSlider"))
        _ = setup_editdoubleslider(
            layout_sl, 2, 0, 2.3, 1.1, function=lambda: print("QEditSlider"), include_buttons=False
        )

        # Switch
        groub_sw, layout_sw = setup_vcollapsiblegroupbox(_layout, "Switch", False)
        _ = setup_label(layout_sw, "QHSwitch")
        _ = setup_hswitch(layout_sw, ["A", "B", "C"], default=1, function=lambda: print("QHSwitch"))
        _ = setup_label(layout_sw, "QVSwitch")
        _ = setup_vswitch(layout_sw, ["A", "B", "C"], default=1, function=lambda: print("QVSwitch"))

        return _container

    def init_page3(self):
        """Initializes and returns the third gallery page.

        Returns:
            QWidget: The third gallery page widget.
        """
        _container = QWidget()
        _layout = QVBoxLayout(_container)
        _container.setMinimumWidth(230)
        _container.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        _layout.setAlignment(Qt.AlignTop)

        # Progressbar
        groub_pb, layout_pb = setup_vcollapsiblegroupbox(_layout, "Progressbar", False)
        _ = setup_label(layout_pb, "QProgressBar")
        _ = setup_progressbar(layout_pb, 0, 100, 10, True)
        _ = setup_label(layout_pb, "QProgressbarEdit")
        _ = setup_progressbaredit(layout_pb, 0, 100, 10, function=lambda: print("QProgressbarEdit"))

        # Layer Select
        groub_ls, layout_ls = setup_vcollapsiblegroupbox(_layout, "QLayerSelect", False)
        _ = setup_label(layout_ls, "Select an Image Layer")
        _ = setup_layerselect(
            layout_ls, self._viewer, Image, function=lambda: print("QLayerSelect")
        )
        _ = setup_label(layout_ls, "Select an Labels Layer")
        _ = setup_layerselect(
            layout_ls, self._viewer, Labels, function=lambda: print("QLayerSelect")
        )

        # Colorbar
        groub_co, layout_co = setup_vcollapsiblegroupbox(_layout, "Color", False)
        _ = setup_label(layout_co, "Colorbar")
        _ = setup_colorbar(layout_co, "viridis")
        _ = setup_colorbar(layout_co, "jet")

        # Colorpicker
        _ = setup_label(layout_co, "QColorPicker")
        _ = setup_colorpicker(layout_co, [0, 100, 167], function=lambda: print("QColorPicker"))
        _ = setup_label(layout_co, "QEditColorPicker")
        _ = setup_editcolorpicker(
            layout_co, [167, 100, 0], function=lambda: print("QEditColorPicker")
        )

        # Dialogs
        groub_dia, layout_dia = setup_vcollapsiblegroupbox(_layout, "Dialogs", False)
        # QFileSelect
        _ = setup_label(layout_dia, "QFileSelect")
        _ = setup_fileselect(layout_dia, function=lambda: print("QFileSelect"))
        # QFileSelect
        _ = setup_label(layout_dia, "QFileSelect(save directory)")
        _ = setup_savefileselect(layout_dia, function=lambda: print("QFileSelect(save directory)"))
        # QFileSelect
        _ = setup_label(layout_dia, "QDirSelect")
        _ = setup_dirselect(layout_dia, function=lambda: print("QDirSelect"))
        # QDateTimeEdit
        _ = setup_label(layout_dia, "QDateTimeEdit")
        _ = setup_timeedit(layout_dia)

        # Icons
        groub_icn, layout_icn = setup_vcollapsiblegroupbox(_layout, "Icons", False)
        btn = setup_pushbutton(layout_icn, "Button", function=lambda: print("QPushButton"))
        sld = setup_slider(layout_icn, function=lambda: print("QSlider"))
        spn = setup_spinbox(layout_icn, function=lambda: print("QSpinBox"))

        _icon_dict = {True: "check", False: "delete_shape", "Something": "lock_open"}
        _color_dict = {True: "green", False: "red", "Something": "lightblue"}

        _ = setup_icon_wrapper(btn, icon_dict=_icon_dict, color_dict=_color_dict, default=True)
        _ = setup_icon_wrapper(sld, icon_dict=_icon_dict, color_dict=_color_dict, default=False)
        _ = setup_icon_wrapper(
            spn, icon_dict=_icon_dict, color_dict=_color_dict, default="Something"
        )

        return _container

    def init_page4(self):
        """Initializes and returns the fourth gallery page.

        Returns:
            QWidget: The fourth gallery page widget.
        """
        _container = QWidget()
        _layout = QVBoxLayout(_container)
        _container.setMinimumWidth(230)
        _container.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        _layout.setAlignment(Qt.AlignTop)

        # Datastructs
        groub_ds, layout_ds = setup_vcollapsiblegroupbox(_layout, "Data Structs", False)
        _ = setup_label(layout_ds, "QTableWidget")
        _ = setup_table(
            layout_ds,
            [[1, 2, 3], [1, 3, 4], [1, 5, 6]],
            ["A", "B", "C"],
            function=lambda: print("QTableWidget"),
        )
        _ = setup_label(layout_ds, "QListWidget")
        _ = setup_list(layout_ds, ["A", "B", "C"], True, function=lambda: print("QListWidget"))
        _ = setup_label(layout_ds, "QTreeWidget")
        _tree = setup_tree(layout_ds, ["Name", "Value"], function=lambda: print("QTreeWidget"))
        t1 = QTreeWidgetItem(_tree, ["Parent Item", "10"])
        _ = QTreeWidgetItem(t1, ["Child 1", "20"])
        _ = QTreeWidgetItem(t1, ["Child 2", "30"])

        # Acknowledgements
        _ = setup_acknowledgements(_layout)
        return _container


def show_widget_gallery() -> None:
    """Launches a Napari viewer and displays the widget gallery.

    This function creates a new Napari viewer, initializes the `GalleryWidget`,
    and adds it as a dock widget to the right side of the viewer window.

    The function then starts the Napari event loop.
    """
    viewer = napari.Viewer()

    widget = GalleryWidget(viewer)
    viewer.window.add_dock_widget(widget, area="right")

    napari.run()


if __name__ == "__main__":
    show_widget_gallery()
