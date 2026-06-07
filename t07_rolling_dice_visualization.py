"""
Visualisation: Monte Carlo vs Analytical Dice Probabilities
Reads results.json produced by simulation.py and generates two figures:
    1. bar_comparison.png  - side-by-side bar chart (Monte Carlo vs analytical)
    2. deviation_plot.png  - absolute deviation per sum
"""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Variables
RESULT_JSON = "t07_results.json"
BAR_COMPARISON_FILE_NAME = "bar_comparison.png"
DEVIATION_PLOT_FILE_NAME = "deviation_plot.png"

DATA_FILE = Path(__file__).parent / RESULT_JSON

# Load data
with DATA_FILE.open() as f:
    data = json.load(f)

n_sims   = data["simulations"]
sim_vals = {int(k): v for k, v in data["simulated"].items()}
ana_vals = {int(k): v for k, v in data["analytical"].items()}

sums = list(range(2, 13))
sim = np.array([sim_vals[s] * 100 for s in sums])
ana = np.array([ana_vals[s] * 100 for s in sums])
dev = np.abs(sim - ana)

FIGS = Path(__file__).parent / "t07_figures"
FIGS.mkdir(exist_ok=True)

# Shared style
BLUE = "#3266AD"
RED  = "#C0392B"
GRAY = "#7F8C8D"
BG   = "#FAFAFA"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.facecolor": BG,
    "figure.facecolor": BG,
})

# Figure 1: side-by-side bar chart
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(sums))
width = 0.38

bars_sim = ax.bar(
    x - width / 2, sim, width, label="Monte Carlo",
    color=BLUE, alpha=0.88, zorder=3, linewidth=0
)
bars_ana = ax.bar(
    x + width / 2, ana, width, label="Analytical",
    color=RED, alpha=0.72, zorder=3, linewidth=0
)

# Value labels
for bar in bars_sim:
    h = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2, h + 0.08,
        f"{h:.2f}%", ha="center", va="bottom", fontsize=8, color=BLUE
    )
for bar in bars_ana:
    h = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2, h + 0.08,
        f"{h:.2f}%", ha="center", va="bottom", fontsize=8, color=RED
    )

ax.set_xticks(x)
ax.set_xticklabels([str(s) for s in sums])
ax.set_xlabel("Sum of two dice", fontsize=12)
ax.set_ylabel("Probability (%)", fontsize=12)
ax.set_title(
    f"Monte Carlo vs Analytical Probabilities\n({n_sims:,} simulations)",
    fontsize=14, fontweight="bold", pad=14,
)
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
ax.legend(fontsize=11, framealpha=0.7)
ax.set_ylim(0, max(ana) * 1.25)

fig.tight_layout()
out1 = FIGS / BAR_COMPARISON_FILE_NAME
fig.savefig(out1, dpi=150)
plt.close(fig)
print(f"Saved -> {out1}")


# Figure 2: deviation plot
fig, ax = plt.subplots(figsize=(11, 4.5))

colours = [RED if d > 0.05 else BLUE if d > 0.01 else "#27AE60" for d in dev]
ax.bar(sums, dev, color=colours, alpha=0.82, zorder=3, linewidth=0)

threshold = 0.05
ax.axhline(threshold, color=RED, linewidth=1.2, linestyle="--", alpha=0.7,
           label=f"0.05% threshold")

for s, d, c in zip(sums, dev, colours):
    ax.text(s, d + 0.003, f"{d:.4f}%", ha="center", va="bottom",
            fontsize=8, color=c)

ax.set_xticks(sums)
ax.set_xlabel("Sum of two dice", fontsize=12)
ax.set_ylabel("|Difference| (%)", fontsize=12)
ax.set_title(
    "Absolute Deviation: Monte Carlo vs Analytical",
    fontsize=14, fontweight="bold", pad=14,
)
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)

legend_patches = [
    mpatches.Patch(color="#27AE60", label="< 0.01% (excellent)"),
    mpatches.Patch(color=BLUE, label="0.01 - 0.05% (good)"),
    mpatches.Patch(color=RED, label="> 0.05% (notable)"),
]
ax.legend(handles=legend_patches, fontsize=10, framealpha=0.7)

fig.tight_layout()
out2 = FIGS / DEVIATION_PLOT_FILE_NAME
fig.savefig(out2, dpi=150)
plt.close(fig)
print(f"Saved -> {out2}")