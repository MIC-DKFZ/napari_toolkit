"""Binding-neutral import checks run once for each tox Qt binding factor."""

import os

import pytest
import qtpy


@pytest.mark.parametrize(
    "module",
    [
        "napari_toolkit.widget_gallery",
        "napari_toolkit.containers",
        "napari_toolkit.data_structs",
        "napari_toolkit.utils",
        "napari_toolkit.widgets",
    ],
)
def test_public_modules_import_with_selected_qt_binding(module):
    """All public modules must load with the binding selected by ``QT_API``."""
    __import__(module)

    requested_api = os.environ.get("QT_API")
    if requested_api:
        assert qtpy.API_NAME.lower() == requested_api.lower()


def test_colorbar_uses_binding_neutral_matplotlib_qt_canvas():
    """The colorbar must use Matplotlib's Qt5/Qt6-neutral canvas module."""
    from napari_toolkit.widgets.color.colorbar import FigureCanvas

    assert FigureCanvas.__module__ == "matplotlib.backends.backend_qtagg"
