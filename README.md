# napari-toolkit

Toolkit to handle  QWidgets for Napari Plugins.

----------------------------------

#### Buttons
- QPushButton
- QRadioButton
- QToggleButton

#### Spinbox
- QSpinBox
- QDoubleSpinBox

#### Progressbar
- QProgressBar
- QProgressbarEdit

#### Slider
- QSlider
- QLabelSlider
- QSliderEdit
- QFloatSlider
- QFloatLabelSlider
- QFloatSliderEdit - TODO

#### Text
- QLabel
- QLineEdit
- QTextEdit
- QPlainTextEdit

#### Groupbox
- QGroupBox
- QCollapsableGroupBox

#### QComboBox
- QComboBox

#### Checkbox
- QCheckBox

#### Switch
- QVSwitch
- QHSwitch


# Common Widgets

- QPushButton: A clickable button (e.g., Start, Stop, or Run).
- QSlider: A horizontal or vertical slider for selecting a value within a range. 
- QSpinBox: A spin box for numeric input with up/down buttons. 
- QDoubleSpinBox: Similar to QSpinBox but supports floating-point numbers. 
- QLabel: A label to display text, images, or other static content. 
- QLineEdit: A single-line text input box. 
- QTextEdit: A multi-line text box for editing/displaying text
- QPlainTextEdit: Similar to QTextEdit, optimized for plain text (faster for large text). 
- QComboBox: A dropdown list for selecting one item from multiple options. 
- QCheckBox: A checkbox for toggling a boolean option (checked/unchecked). 
- QRadioButton: A radio button for selecting one option in a group. 
- QProgressBar: A progress bar to indicate completion of a task.

# Containers and Layouts

- QGroupBox: A container with a title for grouping related widgets. 
- QTabWidget: A tabbed interface to organize content into separate tabs. 
- QVBoxLayout / QHBoxLayout: Vertical and horizontal layouts for organizing widgets. 
- QStackedWidget: A stack of widgets where only one is visible at a time.
- QScrollArea

# Advanced Input Widgets

- QColorDialog / QColorButton: Widgets for selecting colors.
        Note: QColorDialog is a dialog; QColorButton is custom (Napari-specific).
- QFileDialog: A dialog to select files or directories (can be embedded into a plugin).
- QListWidget: A list widget to display and select items.
- QTreeWidget: A tree structure for hierarchical data. 
- QTableWidget: A table/grid for displaying tabular data.
- QDateTimeEdit: Input for date and time values.

# Custom
- QLayerSelect
- QHSwitch
- QVSwitch
- QFloatSlider
- QFloatLabelSlider
- QLabelSlider
- QCollapsableGroupBox


----------------------------------



This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-toolkit` via [pip]:

    pip install napari-toolkit




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [Apache Software License 2.0] license,
"napari-toolkit" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
