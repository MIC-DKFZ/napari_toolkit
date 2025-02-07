from typing import Optional

from napari.layers import Image, Labels
from napari.viewer import Viewer
from qtpy.QtWidgets import QHBoxLayout, QSizePolicy, QTreeWidgetItem, QVBoxLayout, QWidget

from napari_toolkit.layout.boxlayout import hstack, vstack
from napari_toolkit.layout.collabsable_groubox import (
    add_collabsgroupbox,
    add_hcollabsgroupbox,
    add_vcollabsgroupbox,
)
from napari_toolkit.layout.groupbox import add_hgroupbox, add_vgroupbox
from napari_toolkit.layout.icon import add_icon
from napari_toolkit.setup.button import setup_button, setup_radiobutton, setup_togglebutton
from napari_toolkit.setup.checkbox import setup_checkbox
from napari_toolkit.setup.colorbar import setup_colorbar
from napari_toolkit.setup.combobox import setup_combobox
from napari_toolkit.setup.data_structs import setup_list, setup_table, setup_tree
from napari_toolkit.setup.dialog import (
    setup_colorpicker,
    setup_dirselect,
    setup_fileselect,
    setup_savefileselect,
    setup_timeedit,
)
from napari_toolkit.setup.layer_select import setup_layerselect
from napari_toolkit.setup.progressbar import setup_progressbar, setup_progressbaredit
from napari_toolkit.setup.slider import (
    setup_editfloatslider,
    setup_editslider,
    setup_floatslider,
    setup_labelfloatslider,
    setup_labelslider,
    setup_slider,
)
from napari_toolkit.setup.spinbox import setup_doublespinbox, setup_spinbox
from napari_toolkit.setup.switch import setup_hswitch, setup_vswitch
from napari_toolkit.setup.text_edit import (
    setup_label,
    setup_lineedit,
    setup_plaintextedit,
    setup_textedit,
)


class TestWidget(QWidget):
    def __init__(self, viewer: Viewer, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._viewer = viewer
        _main_layout = QVBoxLayout(self)
        self.setFixedWidth(300)

        # BUTTONS
        groub_btn, layout_btn = add_vcollabsgroupbox(_main_layout, "Buttons", True)
        _ = setup_button(layout_btn, "Button", function=lambda: print("Button"))
        layout_rbtn = QHBoxLayout()
        layout_btn.addLayout(layout_rbtn)
        _ = setup_radiobutton(
            layout_rbtn, "Radiobutton", False, function=lambda: print("Radiobutton")
        )
        _ = setup_radiobutton(
            layout_rbtn, "Radiobutton2", True, function=lambda: print("Radiobutton2")
        )
        layout_tbtn = QHBoxLayout()
        layout_btn.addLayout(layout_tbtn)
        _ = setup_togglebutton(layout_tbtn, "ToggleButton", function=lambda: print("ToggleButton"))
        _ = setup_togglebutton(
            layout_tbtn, "ToggleButton", True, function=lambda: print("ToggleButton")
        )

        # SPINBOX
        groub_sb, layout_sb = add_vcollabsgroupbox(_main_layout, "SpinBox", True)
        _ = setup_spinbox(layout_sb, 0, 25, 1, 5, function=lambda: print("SpinBox"))
        _ = setup_doublespinbox(
            layout_sb, 0, 25.5, 0.05, 2, function=lambda: print("DoubleSpinbox"), digits=3
        )

        # Slider
        groub_sl, layout_sl = add_vcollabsgroupbox(_main_layout, "Slider", True)
        _ = setup_slider(layout_sl, 0, 50, 10, 30, function=lambda: print("Slider"))
        _ = setup_labelslider(layout_sl, 0, 50, 5, 30, function=lambda: print("Slider"))
        _ = setup_editslider(layout_sl, function=lambda: print("QSliderEdit"))
        # FloatSlider
        _ = setup_floatslider(layout_sl, 2, 0, 1, 0.5, function=lambda: print("QFloatSlider"))
        _ = setup_labelfloatslider(layout_sl, 2, 0, 2.3, 1, 1.0, function=lambda: print("Slider"))
        _ = setup_editfloatslider(layout_sl, 2, 0, 2.3, 1, function=lambda: print("Slider"))

        # Progressbar
        groub_pb, layout_pb = add_vcollabsgroupbox(_main_layout, "Progressbar", True)
        _ = setup_progressbar(layout_pb, 0, 100, 10, True)
        _ = setup_progressbaredit(
            layout_pb, 0, 100, 10, function=lambda: print("ProgressSyncWidget")
        )

        # Text Edit
        groub_tx, layout_tx = add_vcollabsgroupbox(_main_layout, "Text Edit", True)
        _ = setup_label(layout_tx, "QLabel")
        _ = setup_lineedit(layout_tx, "QLineEdit", "QLineEdit", function=lambda: print("QLineEdit"))
        _ = setup_textedit(layout_tx, "QTextEdit", "QTextEdit", function=lambda: print("QTextEdit"))
        _ = setup_plaintextedit(
            layout_tx, "QPlainTextEdit", "QPlainTextEdit", function=lambda: print("QPlainTextEdit")
        )

        # Switch
        groub_sw, layout_sw = add_vcollabsgroupbox(_main_layout, "Switch", True)
        _ = setup_hswitch(layout_sw, ["A", "B", "C"], function=lambda: print("QHSwitch"))
        _ = setup_vswitch(layout_sw, ["A", "B", "C"], function=lambda: print("QVSwitch"))

        # Combobox
        groub_cb, layout_cb = add_vcollabsgroupbox(_main_layout, "Combobox", True)
        _ = setup_combobox(
            layout_cb, ["A", "B", "C"], "QComboBox", function=lambda: print("QComboBox")
        )

        # Checkbox
        groub_ch, layout_ch = add_vcollabsgroupbox(_main_layout, "Checkbox", True)
        _ = setup_checkbox(layout_ch, "QCheckBox", function=lambda: print("QCheckBox"))

        # Layer Select
        groub_ls, layout_ls = add_vcollabsgroupbox(_main_layout, "Layer Select", True)
        _ = setup_layerselect(
            layout_ls, self._viewer, Image, function=lambda: print("QLayerSelect")
        )
        _ = setup_layerselect(
            layout_ls, self._viewer, Labels, function=lambda: print("QLayerSelect")
        )

        # Colorbar
        groub_co, layout_co = add_vcollabsgroupbox(_main_layout, "Colorbar", True)
        _ = setup_colorbar(layout_co, "viridis")
        _ = setup_colorbar(layout_co, "jet")

        # Datastructs
        groub_ds, layout_ds = add_vcollabsgroupbox(_main_layout, "Data Structs", True)
        _ = setup_table(
            layout_ds,
            [[1, 2, 3], [1, 3, 4], [1, 5, 6]],
            ["A", "B", "C"],
            function=lambda: print("QTableWidget"),
        )
        _ = setup_list(layout_ds, ["A", "B", "C"], True, function=lambda: print("QListWidget"))

        _tree = setup_tree(
            layout_ds,
            ["Name", "Value"],
            function=lambda: print("QTreeWidget"),
        )
        t1 = QTreeWidgetItem(_tree, ["Parent Item", "10"])
        _ = QTreeWidgetItem(t1, ["Child 1", "20"])
        _ = QTreeWidgetItem(t1, ["Child 2", "30"])


if __name__ == "__main__":
    import napari
    from qtpy.QtWidgets import QApplication

    app = QApplication([])
    viewer = napari.Viewer()

    # Add the custom widget without installation
    widget = TestWidget(viewer)
    viewer.window.add_dock_widget(widget, area="right")  # Add widget to the right panel

    # Start the Napari event loop
    napari.run()
