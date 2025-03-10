# Napari Toolkit

A napari toolkit for handling QWidgets to simplify the development of Napari plugins.
The toolkit provides enhanced widgets, UI components, and utilities that streamline plugin creation, improve layout management, and enhance user interaction within the Napari ecosystem.


## Installation
#### 1. Install `napari_toolkit`
```shell
pip install napari-toolkit
```
or clone the repository:
```shell
git clone https://github.com/MIC-DKFZ/napari_toolkit.git
cd napari_toolkit
pip install -e ./
```
#### 2. (Optional) Initialize your Plugin
Afterward it is recommended to generate you plugin with [copier] using the [napari-plugin-template].

---

## Gallery

````python
from napari_toolkit.widget_gallery import show_widget_gallery
show_widget_gallery()
````
<img src="imgs/Gallery.png">

## Widgets
````python
from napari_toolkit.widgets import (setup_acknowledgements, setup_checkbox, setup_colorbar,
                                    setup_colorpicker, setup_combobox, setup_dirselect,
                                    setup_doubleslider, setup_doublespinbox, setup_editcolorpicker,
                                    setup_editdoubleslider, setup_editslider, setup_fileselect,
                                    setup_hswitch, setup_icon_wrapper, setup_iconbutton,
                                    setup_label, setup_labeleddoubleslider, setup_labeledslider,
                                    setup_layerselect, setup_lineedit, setup_plaintextedit,
                                    setup_progressbar, setup_progressbaredit, setup_pushbutton,
                                    setup_radiobutton, setup_savefileselect, setup_slider,
                                    setup_spinbox, setup_textedit, setup_timeedit,
                                    setup_togglebutton, setup_vswitch)
````

#### Buttons
- ``QPushButton``: A standard clickable button that can trigger an action.
- ``QRadioButton``: A radio button for selecting one option in a group.
- ``QToggleButton``: A clickable button that toggles between an "on" and "off" state.
- ``IconButton``: A QPushButton with an Icon.
#### Spinbox
- ``QSpinBox``: A numerical input field allowing integer selection with up/down arrows.
- ``QDoubleSpinBox``: A spinbox similar to QSpinBox but supports floating-point numbers.
#### Slider
- ``QSlider``: A horizontal or vertical slider for selecting an integer value.
- ``QDoubleSlider``: A slider that supports floating-point values instead of integers.
- ``QLabeledSlider``: A QSlider combined with a QLabel to display the value.
- ``QLabeledDoubleSlider``: A QFloatSlider with an accompanying QLabel to show the selected value.
- ``QEditSlider``: A QSlider paired with an editable text box for precise input.
- ``QEditDoubleSlider``: A QFloatSlider paired with an editable text box for precise input.
#### Progressbar
- ``QProgressBar``: A visual progress indicator that displays completion percentage.
- ``QProgressbarEdit``: A QProgressBar with an editable field for manual updates.
#### Text Edit
- ``QLabel``: A non-editable text display widget.
- ``QLineEdit``: A single-line text input field.
- ``QTextEdit``: A multi-line text editor with rich-text support
- ``QPlainTextEdit``: A multi-line text editor optimized for plain text input.
#### Switch
- ``QVSwitch``: A vertical switch that toggles between multiple states.
- ``QHSwitch``: A horizontal switch that toggles between multiple states.
#### QComboBox
- ``QComboBox``: A dropdown menu for selecting one option from a list.
#### Checkbox
- ``QCheckBox``: A selectable box that toggles between checked and unchecked states.
#### Color
- ``Colorbar``: A widget displaying a colorbar.
- ``QColorPicker``: A dialog for selecting colors.
- ``QEditColorPicker``:A dialog for selecting colors, combined with a textfield and slider for changing efficiently rgba values.
#### QLayerSelect
- `` QLayerSelect``: A dropdown or list for selecting a specific layer type (Labels, Images,...) in the Napari Viewer.
#### File/Dir Select
- ``QFileSelect``: A file selection dialog to choose a file.
- ``QFileSelect(save directory)``: A file selection dialog specifically for saving directories.
- ``QDirSelect``: A directory selection dialog.
#### QTimeEdit
- ``QDateTimeEdit``: A widget for selecting and editing date and time values.
## Containers
````python
from napari_toolkit.containers import (setup_hgroupbox, setup_scrollarea, setup_tabwidget,
                                       setup_vcollapsiblegroupbox)
````
- ``QGroupBox``: A container with a title for grouping related widgets.
- ``QCollapsableGroupBox``: A QGroupBox that can be expanded or collapsed to show/hide content.
- ``QScrollArea``: A container that allows scrolling when content exceeds available space.
- ``QTabWidget``: A widget with multiple tabs for organizing content.
## Data Struct
````python
from napari_toolkit.data_structs import setup_list, setup_table, setup_tree
````
- ``QListWidget``: A list-based widget that allows displaying and managing a list of items.
- ``QTableWidget``:  A table-based widget that provides an editable grid of rows and columns, commonly used for structured data representation.
- ``QTreeWidget``: A hierarchical tree-based widget that enables organizing data in expandable and collapsible parent-child relationships.


---

## Widget Value Handling

Easily get and set values for QWidgets in your Napari plugin.
**Note:** These functions work for many widgets but are not guaranteed to support all

````python
from napari_toolkit.utils.widget_getter import get_value
from napari_toolkit.utils.widget_setter import set_value

set_value(<QWidget>,<value>)        # Sets the value of widget
_ = get_value(<QWidget>,<value>)    # Retrieves the value of a widget
````

---

## Acknowledgments

<p align="left">
  <img src="imgs/Logos/HI_Logo.png" width="150"> &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="imgs/Logos/DKFZ_Logo.png" width="500">
</p>

This repository is developed and maintained by the Applied Computer Vision Lab (ACVL)
of [Helmholtz Imaging](https://www.helmholtz-imaging.de/).

This [napari] plugin was generated with [copier] using the [napari-plugin-template].


[copier]: https://copier.readthedocs.io/en/stable/
[napari]: https://github.com/napari/napari
[napari-plugin-template]: https://github.com/napari/napari-plugin-template
