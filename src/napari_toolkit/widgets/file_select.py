import os
from typing import Callable, Optional

from qtpy.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from napari_toolkit.utils.utils import connect_widget


class QDirSelect(QWidget):
    """A widget for selecting and displaying a directory path.

    This widget consists of a button to open a directory selection dialog
    and a line edit to display the selected path.

    Attributes:
        default_dir (Optional[str]): The default directory for the selection dialog.
        button (QPushButton): The button that opens the directory selection dialog.
        line_edit (QLineEdit): The read-only field displaying the selected directory.
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        text: str = "Select",
        read_only: bool = True,
        default_dir: Optional[str] = None,
    ) -> None:
        """Initializes the QDirSelect widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            text (str, optional): The label text for the directory selection button. Defaults to "Select".
            read_only (bool, optional): Whether the line edit is read-only. Defaults to True.
            default_dir (Optional[str], optional): The initial directory to open in the dialog. Defaults to None.
        """
        super().__init__(parent)
        self.default_dir = default_dir

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self.button = QPushButton(text)
        self._layout.addWidget(self.button, stretch=1)

        self.line_edit = QLineEdit("")
        self.line_edit.setReadOnly(read_only)
        self._layout.addWidget(self.line_edit, stretch=2)

        self.button.clicked.connect(self.select_directory)

        self.setLayout(self._layout)

    def select_directory(self):
        """Opens a dialog to select a directory and updates the label."""
        _dialog = QFileDialog(self)
        _dialog.setDirectory(os.getcwd() if self.default_dir is None else self.default_dir)

        _output_dir = _dialog.getExistingDirectory(
            self,
            "Select an Output Directory",
            options=QFileDialog.DontUseNativeDialog | QFileDialog.ShowDirsOnly,
        )

    def set_dir(self, directory):
        """Sets the displayed directory in the line edit.

        Args:
            directory (str): The directory path to display.
        """
        self.line_edit.setText(f"{directory}")

    def get_dir(self):
        """Retrieves the currently selected directory.

        Returns:
            str: The currently displayed directory path.
        """
        return self.line_edit.text()


class QFileSelect(QWidget):
    """A widget for selecting and displaying a file path.

    This widget provides a button to open a file selection dialog and a line
    edit field to display the selected file path.

    Attributes:
        default_dir (Optional[str]): The default directory for the file selection dialog.
        save_file (bool): Whether the widget should open a save file dialog instead of an open file dialog.
        filtering (Optional[str]): A filter string for restricting file types (e.g., "Images (*.png *.jpg)").
        button (QPushButton): The button that opens the file selection dialog.
        line_edit (QLineEdit): The read-only field displaying the selected file path.
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        filtering: Optional[str] = None,
        text: str = "Select",
        read_only: bool = True,
        default_dir: Optional[str] = None,
        save_file: bool = False,
    ) -> None:
        """Initializes the QFileSelect widget.

        Args:
            parent (Optional[QWidget], optional): The parent widget. Defaults to None.
            filtering (Optional[str], optional): A filter string to restrict file types (e.g., "Images (*.png *.jpg)"). Defaults to None.
            text (str, optional): The label text for the file selection button. Defaults to "Select".
            read_only (bool, optional): Whether the line edit is read-only. Defaults to True.
            default_dir (Optional[str], optional): The initial directory to open in the dialog. Defaults to None.
            save_file (bool, optional): Whether the widget should open a save file dialog instead of an open file dialog. Defaults to False.
        """

        super().__init__(parent)
        self.default_dir = default_dir
        self.save_file = save_file
        self.filtering = filtering

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self.button = QPushButton(text)
        self._layout.addWidget(self.button, stretch=1)

        self.line_edit = QLineEdit("")
        self.line_edit.setReadOnly(read_only)
        self._layout.addWidget(self.line_edit, stretch=2)

        self.button.clicked.connect(self.select_file)

        self.setLayout(self._layout)

    def select_file(self):
        """Opens a dialog to select a directory and updates the label."""
        _dialog = QFileDialog(self)
        _dialog.setDirectory(os.getcwd() if self.default_dir is None else self.default_dir)

        if self.save_file:
            _output_file, _filter = _dialog.getSaveFileName(
                self, "Select File", filter=self.filtering, options=QFileDialog.DontUseNativeDialog
            )
        else:
            _output_file, _filter = _dialog.getOpenFileName(
                self, "Select File", filter=self.filtering, options=QFileDialog.DontUseNativeDialog
            )
        if _filter != "":
            self.set_file(_output_file)

    def set_file(self, directory):
        """Sets the displayed file path in the line edit.

        Args:
            file_path (str): The file path to display.
        """
        self.line_edit.setText(f"{directory}")

    def get_file(self):
        """Retrieves the currently selected file path.

        Returns:
            str: The currently displayed file path.
        """
        return self.line_edit.text()


def setup_fileselect(
    layout: QLayout,
    text: str = "Select",
    read_only: bool = True,
    default_dir: str = None,
    filtering: str = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates and adds a file selection widget to the given layout.

    This function initializes a `QFileSelect` widget configured for selecting
    existing files and integrates it into the provided layout.

    Args:
        layout (QLayout): The layout to which the file selection widget will be added.
        text (str, optional): The label text for the file selection button. Defaults to "Select".
        read_only (bool, optional): Whether the file path field is read-only. Defaults to True.
        default_dir (Optional[str], optional): The initial directory to open in the dialog. Defaults to None.
        filtering (Optional[str], optional): A filter string to restrict file types (e.g., "Images (*.png *.jpg)"). Defaults to None.
        function (Optional[Callable[[], None]], optional): A callback function triggered when a file is selected. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized `QFileSelect` widget.
    """

    _widget = QFileSelect(
        text=text,
        filtering=filtering,
        read_only=read_only,
        default_dir=default_dir,
        save_file=False,
    )
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.button.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_savefileselect(
    layout: QLayout,
    text: str = "Select",
    read_only: bool = True,
    default_dir: str = None,
    filtering: str = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates and adds a file selection widget for saving files to the given layout.

    This function initializes a `QFileSelect` widget configured for saving files
    and integrates it into the provided layout.

    Args:
        layout (QLayout): The layout to which the save file selection widget will be added.
        text (str, optional): The label text for the file selection button. Defaults to "Select".
        read_only (bool, optional): Whether the file path field is read-only. Defaults to True.
        default_dir (Optional[str], optional): The initial directory to open in the dialog. Defaults to None.
        filtering (Optional[str], optional): A filter string to restrict file types (e.g., "Text Files (*.txt)"). Defaults to None.
        function (Optional[Callable[[], None]], optional): A callback function triggered when a file is selected. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized `QFileSelect` widget for saving files.
    """
    _widget = QFileSelect(
        text=text, filtering=filtering, read_only=read_only, default_dir=default_dir, save_file=True
    )
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.button.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )


def setup_dirselect(
    layout: QLayout,
    text: str = "Select",
    read_only: bool = True,
    default_dir: str = None,
    function: Optional[Callable] = None,
    tooltips: Optional[str] = None,
    shortcut: Optional[str] = None,
    stretch: int = 1,
) -> QWidget:
    """Creates and adds a directory selection widget to the given layout.

    This function initializes a `QDirSelect` widget configured for selecting directories
    and integrates it into the provided layout.

    Args:
        layout (QLayout): The layout to which the directory selection widget will be added.
        text (str, optional): The label text for the directory selection button. Defaults to "Select".
        read_only (bool, optional): Whether the directory path field is read-only. Defaults to True.
        default_dir (Optional[str], optional): The initial directory to open in the dialog. Defaults to None.
        function (Optional[Callable[[], None]], optional): A callback function triggered when a directory is selected. Defaults to None.
        tooltips (Optional[str], optional): Tooltip text for the widget. Defaults to None.
        shortcut (Optional[str], optional): A keyboard shortcut for quick access. Defaults to None.
        stretch (int, optional): The stretch factor in the layout. Defaults to 1.

    Returns:
        QWidget: The initialized `QDirSelect` widget.
    """
    _widget = QDirSelect(text=text, read_only=read_only, default_dir=default_dir)
    _widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return connect_widget(
        layout,
        _widget,
        widget_event=_widget.button.clicked,
        function=function,
        shortcut=shortcut,
        tooltips=tooltips,
        stretch=stretch,
    )
