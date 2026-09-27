"""Regenerates the 'Target Distribution: Alert Outcomes' chart for the EDA site.

Fixes a layout bug in the original chart: the per-bar count/percentage
annotation on the tallest bar was placed so close to the top of the axes
that it visually collided with the plot title. This version adds vertical
headroom above the tallest bar (via ylim) and extra title padding so the
annotation and title never overlap regardless of bar height.
"""
import matplotlib.pyplot as plt

# Counts from train_signals['eskalatsiya'].value_counts() (14000 alerts total).
counts = {
    "Dismissed (0)": 11595,
    "Escalated (1)": 2405,
}
colors = ["#4C72B0", "#C44E52"]
total = sum(counts.values())

fig, ax = plt.subplots(figsize=(6, 4.5), dpi=100)
bars = ax.bar(counts.keys(), counts.values(), color=colors)

# Headroom above the tallest bar so the annotation never reaches the title.
ax.set_ylim(0, max(counts.values()) * 1.22)

for bar, count in zip(bars, counts.values()):
    pct = count / total * 100
    ax.annotate(
        f"{count}\n({pct:.1f}%)",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

ax.set_title("Target Distribution: Alert Outcomes", pad=15)
ax.set_ylabel("Number of alerts")
fig.tight_layout()
fig.savefig("target_distribution.png", dpi=100)
print("saved target_distribution.png")
