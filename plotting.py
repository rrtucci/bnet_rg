import subprocess
import tempfile
import os

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.image as mpimg
from matplotlib.gridspec import GridSpec


def plot_dot_with_colorbar(
    dot_file,
    caption,
    cmap_name="viridis",
    vmin=0.0,
    vmax=1.0,
    figsize=(8, 4),
    colorbar_label="Efficiency"
):
    with tempfile.TemporaryDirectory() as tmp:
        png_file = os.path.join(tmp, "graph.png")

        # Render DOT -> PNG
        subprocess.run(
            ["neato", "-Tpng", dot_file, "-o", png_file],
            check=True
        )

        # Load PNG
        img = mpimg.imread(png_file)

        fig = plt.figure(figsize=figsize)
        gs = GridSpec(1, 2, width_ratios=[4, 0.3])

        ax_graph = fig.add_subplot(gs[0])
        ax_graph.imshow(img)
        ax_graph.axis("off")

        ax_cbar = fig.add_subplot(gs[1])
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
        cbar = plt.colorbar(
            cm.ScalarMappable(norm=norm, cmap=cmap_name),
            cax=ax_cbar
        )
        cbar.set_label(colorbar_label)
        if caption is not None:
            fig.text(
                0.5, 0.01,
                caption,
                ha="center",
                va="bottom"
            )

        plt.tight_layout()
        plt.show()
