import importlib.resources

from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QGroupBox, QLabel, QLayout, QSizePolicy, QSpacerItem, QVBoxLayout


def setup_acknowledgements(layout: QLayout, width: int = 300) -> QGroupBox:
    """Creates and adds an acknowledgements group box to the given layout.

    This function loads logos from the `napari_toolkit.resources` package, scales them,
    and displays them inside a `QGroupBox` with a white background.

    Args:
        layout (QLayout): The layout to which the acknowledgements group box will be added.
        width (int, optional): The width to which the logos should be scaled. Defaults to 300.

    Returns:
        QGroupBox: The initialized acknowledgements group box.
    """
    _group_box = QGroupBox("")

    _group_box.setStyleSheet(
        """
        QGroupBox {
            background-color: white;
        }
    """
    )

    _layout = QVBoxLayout()

    path_resources = importlib.resources.files("napari_toolkit.resources")
    path_DKFZ = path_resources.joinpath("DKFZ_Logo.png")
    path_HI = path_resources.joinpath("HI_Logo.png")

    pixmap_DKFZ = QPixmap(str(path_DKFZ))
    pixmap_HI = QPixmap(str(path_HI))

    pixmap_DKFZ = pixmap_DKFZ.scaledToWidth(width, Qt.SmoothTransformation)
    pixmap_HI = pixmap_HI.scaledToWidth(width, Qt.SmoothTransformation)

    logo_DKFI = QLabel()
    logo_HI = QLabel()

    logo_DKFI.setPixmap(pixmap_DKFZ)
    logo_HI.setPixmap(pixmap_HI)
    spacer = QSpacerItem(width, 20, QSizePolicy.Minimum)  # , QSizePolicy.Expanding)

    _layout.addWidget(logo_HI)
    _layout.addSpacerItem(spacer)
    _layout.addWidget(logo_DKFI)

    _group_box.setLayout(_layout)
    layout.addWidget(_group_box)
    return _group_box
