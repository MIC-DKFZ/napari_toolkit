from typing import Tuple

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from qtpy.QtWidgets import QLayout, QWidget

matplotlib.use("Qt5Agg")


def get_colorbar(
    colormap_name: str,
    text_low: str = "low",
    text_high: str = "high",
    color_low: str = "white",
    color_high: str = "black",
    figsize: Tuple[float, float] = (1, 0.3),
):
    """Generate a horizontal colorbar with custom labels and colors.

    This function creates a horizontal colorbar using a specified colormap, with
    customizable labels and text colors for the low and high ends. The figure background
    is set to transparent, and axis ticks and labels are removed.

    Args:
        colormap_name (str): Name of the colormap to use (e.g., "viridis", "coolwarm").
        text_low (str, optional): Label for the low end of the colorbar. Defaults to "low".
        text_high (str, optional): Label for the high end of the colorbar. Defaults to "high".
        color_low (str, optional): Text color for the low label. Defaults to "white".
        color_high (str, optional): Text color for the high label. Defaults to "black".
        figsize (Tuple[float, float], optional): Size of the figure in inches (width, height). Defaults to (1, 0.3).

    Returns:
        plt.Figure: The Matplotlib figure containing the colorbar.
    """
    cmap = plt.get_cmap(colormap_name)

    fig, ax = plt.subplots(figsize=figsize)  # Adjust the figure size
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.set_facecolor("none")

    ax.text(
        0.02,
        0.5,
        text_low,
        color=color_low,
        fontsize=12,
        ha="left",
        va="center",
        transform=ax.transAxes,
        fontweight="bold",
    )
    ax.text(
        0.98,
        0.5,
        text_high,
        color=color_high,
        fontsize=12,
        ha="right",
        va="center",
        transform=ax.transAxes,
        fontweight="bold",
    )

    # Create a ScalarMappable and add the colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap)  # , norm=norm)
    sm.set_array([])  # Empty array needed for colorbar
    cb = plt.colorbar(sm, cax=ax, orientation="horizontal")  # , shrink=0.1, aspect=50)
    cb.outline.set_edgecolor("none")

    # Remove the axis ticks and labels completely
    cb.ax.tick_params(size=0, labelsize=0)  # Remove tick lines and labels
    cb.ax.xaxis.set_ticks_position("none")  # Remove tick positions
    cb.ax.yaxis.set_ticks_position("none")  # Remove tick positions
    cb.ax.set_xticks([])  # Ensure no ticks remain
    cb.ax.set_yticks([])

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig


def setup_colorbar(
    layout: QLayout,
    colormap: str = "viridis",
    text_low: str = "low",
    text_high: str = "high",
    color_low: str = "white",
    color_high: str = "black",
    figsize: Tuple[float, float] = (1, 0.3),
) -> QWidget:
    """Create a colorbar and add it to a layout.

    This function generates a colorbar using a specified colormap and custom labels.
    The colorbar is embedded into a Qt layout using a Matplotlib FigureCanvas.

    Args:
        layout (QLayout): The layout to which the colorbar will be added.
        colormap (str, optional): Name of the colormap to use. Defaults to "viridis".
        text_low (str, optional): Label for the low end of the colorbar. Defaults to "low".
        text_high (str, optional): Label for the high end of the colorbar. Defaults to "high".
        color_low (str, optional): Text color for the low label. Defaults to "white".
        color_high (str, optional): Text color for the high label. Defaults to "black".
        figsize (Tuple[float, float], optional): Size of the colorbar figure (width, height). Defaults to (1, 0.3).

    Returns:
        QWidget: The Matplotlib FigureCanvas widget containing the colorbar.
    """
    fig = get_colorbar(colormap, text_low, text_high, color_low, color_high, figsize)
    canvas = FigureCanvas(fig)
    layout.addWidget(canvas)
    return canvas
