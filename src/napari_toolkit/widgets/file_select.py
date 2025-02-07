import os

from qtpy.QtWidgets import QFileDialog, QHBoxLayout, QLineEdit, QPushButton, QWidget


class QDirSelect(QWidget):
    def __init__(self, parent=None, text="Select", read_only=True, default_dir=None):

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
        self.line_edit.setText(f"{directory}")

    def get_dir(self):
        return self.line_edit.text()


class QFileSelect(QWidget):
    def __init__(
        self,
        parent=None,
        filtering=None,
        text="Select",
        read_only=True,
        default_dir=None,
        save_file=False,
    ):

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
                self,
                "Select File",
                filter=self.filtering,
                options=QFileDialog.DontUseNativeDialog,
            )
        else:
            _output_file, _filter = _dialog.getOpenFileName(
                self,
                "Select File",
                filter=self.filtering,
                options=QFileDialog.DontUseNativeDialog,
            )
        if _filter != "":
            self.set_file(_output_file)

    def set_file(self, directory):
        self.line_edit.setText(f"{directory}")

    def get_file(self):
        return self.line_edit.text()
