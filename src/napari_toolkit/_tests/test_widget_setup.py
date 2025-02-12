import pytest
from napari import Viewer
from qtpy.QtWidgets import QApplication, QHBoxLayout, QWidget

from napari_toolkit.widget_gallery import GalleryWidget


@pytest.fixture
def app(qtbot):
    """Fixture to create a Qt Application."""
    return QApplication.instance() or QApplication([])


@pytest.fixture
def viewer():
    """Fixture to create a Napari viewer instance."""
    return Viewer()


def test_gallery_widget(qtbot, viewer):
    """Tests the initialization of the GalleryWidget with a Napari viewer."""

    # Create the GalleryWidget
    widget = GalleryWidget(viewer)

    # Add the widget to the test environment
    qtbot.addWidget(widget)

    # Ensure the widget is a QWidget
    assert isinstance(widget, QWidget)

    # Ensure the widget has a layout
    assert isinstance(widget.layout(), QHBoxLayout)

    # Check if all pages were added to the layout
    layout = widget.layout()
    assert layout.count() == 4, f"Expected 4 pages, found {layout.count()}"

    # Ensure each widget in the layout is valid
    for i in range(layout.count()):
        assert isinstance(layout.itemAt(i).widget(), QWidget), f"Page {i+1} is not a valid QWidget."
