from typing import Callable

from napari.settings import get_settings
from napari.utils.theme import get_theme, register_theme
from napari.viewer import Viewer


def change_theme(viewer: Viewer):
    """Changes the Napari viewer theme to a custom theme with a modified highlight color.

    This function retrieves the current theme settings, modifies the highlight color,
    registers the custom theme, and applies it to the Napari viewer.

    Args:
        viewer (Viewer): The Napari viewer instance.
    """
    settings = get_settings()
    theme = get_theme(settings.appearance.theme)  # Retrieve theme dictionary
    theme.highlight = "rgb(0,100, 167)"

    register_theme("custom", theme, "custom")
    viewer.theme = "custom"
    settings.appearance.theme = "custom"


def get_theme_colors() -> dict:
    """Retrieves the color settings of the currently active Napari theme.

    Returns:
        dict: A dictionary containing theme color mappings.
    """
    theme_name = get_settings().appearance.theme
    theme_colors = get_theme(theme_name)
    return theme_colors


def connect_theme_change(funct: Callable) -> None:
    """Connects a function to the Napari theme change event.

    This allows automatic execution of the given function whenever the theme changes.

    Args:
        funct (Callable): The function to be executed on theme change.
    """
    get_settings().appearance.events.theme.connect(funct)
