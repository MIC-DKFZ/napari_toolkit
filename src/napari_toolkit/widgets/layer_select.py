from napari.layers import Layer
from napari.viewer import Viewer
from qtpy.QtWidgets import QComboBox


class QLayerSelect(QComboBox):
    """
    A QComboBox widget that dynamically updates with the names of layers in a Napari viewer.

    Args:
        parent (Optional[QWidget]): The parent widget.
        layer_type (Optional[Type[Layer]]): A specific Napari layer type to filter by (e.g., Image, Labels).
    """

    def __init__(self, parent=None, layer_type=Layer):
        super().__init__(parent)
        self.layer_type = layer_type
        self.value = self.currentText()
        self.currentIndexChanged.connect(self.update_tooltip)
        self.update_tooltip()
        self.layer_names = {}

    def _update(self, event):
        """
        Updates the combo box with the names of layers in the viewer that match the specified layer type.

        Args:
            event: The Napari event triggered by a layer being added or removed.
        """
        # print(event.type)
        # for attr in dir(event):
        #     if not attr.startswith("_"):  # Skip private attributes
        #         print(f"{attr}: {getattr(event, attr)}")

        if event.type == "removed":
            layer = event.value
            if isinstance(layer, self.layer_type):

                item_index = self.findText(layer.name)
                if item_index != -1:
                    self.removeItem(item_index)
                    del self.layer_names[layer]
        elif event.type == "inserted":
            layer = event.value
            if isinstance(layer, self.layer_type):
                self.addItem(layer.name)
                self.layer_names[layer] = layer.name
                layer.events.name.connect(self._update)
        elif event.type == "name":
            layer = event.source  # The layer that triggered the event
            old_name = self.layer_names.get(layer)
            new_name = layer.name
            self.layer_names[layer] = new_name

            item_index = self.findText(old_name)
            if item_index != -1:  # If the old name exists
                self.setItemText(item_index, new_name)
            else:
                self.addItem(new_name)

    def connect(self, viewer: Viewer):
        """
        Connects the widget to the Napari viewer's layer events to update the combo box
        when layers are added or removed.

        Args:
            viewer (Viewer): The Napari viewer instance to connect to.
        """

        viewer.layers.events.inserted.connect(self._update)
        viewer.layers.events.removed.connect(self._update)
        self.layer_names = {
            layer: layer.name
            for layer in viewer.layers
            if self.layer_type is None or isinstance(layer, self.layer_type)
        }
        for layer in self.layer_names:
            layer.events.name.connect(self._update)

        self.addItems(list(self.layer_names.values()))

    def update_tooltip(self):
        # Set the tooltip to the current item’s text
        self.setToolTip(self.currentText())
