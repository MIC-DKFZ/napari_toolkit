import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def get_colorbar(
    colormap_name,
    text_low="low",
    text_high="high",
    color_low="white",
    color_high="black",
    figsize=(1, 0.3),
):
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


def add_colorbar(
    layout,
    colormap="viridis",
    text_low="low",
    text_high="high",
    color_low="white",
    color_high="black",
    figsize=(1, 0.3),
):
    fig = get_colorbar(colormap, text_low, text_high, color_low, color_high, figsize)
    canvas = FigureCanvas(fig)
    layout.addWidget(canvas)
    return canvas
