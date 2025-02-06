from qtpy.QtCore import Signal
from qtpy.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QWidget,
)


class QProgressbarEdit(QWidget):
    index_changed = Signal()

    def __init__(self, parent=None, min_value=0, max_value=100, start_value=0):
        super().__init__(parent)

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = start_value
        self.init_ui()
        self.setContentsMargins(0, 0, 0, 0)

    def init_ui(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(self.min_value)
        self.progress_bar.setMaximum(self.max_value)
        self.progress_bar.setValue(self.current_value)
        self.progress_bar.setFormat("%v/%m")
        self.progress_bar.setContentsMargins(0, 0, 0, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.current_value))
        self.line_edit.returnPressed.connect(self.update_progress)
        self.line_edit.setContentsMargins(0, 0, 0, 0)

        self.next_button = QPushButton("+", self)
        self.next_button.clicked.connect(self.increment_value)
        self.next_button.setContentsMargins(0, 0, 0, 0)

        self.prev_button = QPushButton("-", self)
        self.prev_button.clicked.connect(self.decrement_value)
        self.prev_button.setContentsMargins(0, 0, 0, 0)

        self.progress_bar.setFixedHeight(self.line_edit.sizeHint().height())

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.progress_bar, stretch=10)
        layout.addWidget(self.prev_button, stretch=2)
        layout.addWidget(self.line_edit, stretch=3)
        layout.addWidget(self.next_button, stretch=2)

        self.setLayout(layout)

    def update_progress(self):
        try:
            value = int(self.line_edit.text())
            self.set_value(value)
        except ValueError:
            pass

    def set_value(self, value):
        if 0 <= value <= self.max_value:
            self.current_value = value
            self.line_edit.setText(str(self.current_value))
            self.progress_bar.setValue(self.current_value)
            self.index_changed.emit()

    def increment_value(self):
        self.set_value(self.current_value + 1)

    def decrement_value(self):
        self.set_value(self.current_value - 1)
