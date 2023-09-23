import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load data from the CSV files into pandas DataFrames.
# Note: The filenames in the provided code were different, make sure to use the correct filenames.
raft = pd.read_csv('raft.csv')
pineapple = pd.read_csv('pineapple.csv')

raft_rmw_p50_values = raft[raft['type'] == 'RMW']['p50']
raft_rmw_p90_values = raft[raft['type'] == 'RMW']['p90']
raft_read_p50_values = raft[raft['type'] == 'Read']['p50']
raft_read_p90_values = raft[raft['type'] == 'Read']['p90']

pineapple_rmw_p50_values = pineapple[pineapple['type'] == 'RMW']['p50']
pineapple_rmw_p90_values = pineapple[pineapple['type'] == 'RMW']['p90']
pineapple_read_p50_values = pineapple[pineapple['type'] == 'Read']['p50']
pineapple_read_p90_values = pineapple[pineapple['type'] == 'Read']['p90']



# Specify the columns we're interested in plotting.
columns = ['p50-read', 'p50-RMW', "p-90-read", "p90-RMW"]

# Extract the values from the chosen columns for each dataset.
raft_values = [
  raft_read_p50_values,
  raft_rmw_p50_values,
  raft_read_p90_values,
  raft_rmw_p90_values,
]
pineapple_values = [
  pineapple_read_p50_values,
  pineapple_rmw_p50_values,
  pineapple_read_p90_values,
  pineapple_rmw_p90_values,
]

# Calculate the median values for the bar chart.
raft_medians = [np.median(val) for val in raft_values]
pineapple_medians = [np.median(val) for val in pineapple_values]

# Set up a new figure and axis for plotting with specified size.
fig, ax = plt.subplots(figsize=(5, 2))

# Define positions for the box plots and bar charts.
positions = np.arange(len(columns))

# Create bar charts representing the median values for each dataset.
ax.bar(positions * 2, raft_medians, width=0.6, alpha=1, label='Raft')
ax.bar(positions * 2 + 1, pineapple_medians, width=0.6, alpha=1, label='Pineapple')

# Create box plots for each dataset.
raftBox = ax.boxplot(raft_values, positions=positions * 2, widths=0.6, patch_artist=True, boxprops=dict(facecolor="blue"))
pineappleBox = ax.boxplot(pineapple_values, positions=positions * 2 + 1, widths=0.6, patch_artist=True, boxprops=dict(facecolor="orange"))

# Set up the x-axis labels and y-axis ticks and limits.
ax.set_xticks(positions*2 + 0.5)
ax.set_xticklabels(columns, rotation=60, ha='right')
ax.set_yticks([0, 1000, 2000, 3000, 4000, 5000, ])
ax.set_ylim(bottom=0)

# Add a legend to the plot.
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Add a y-axis label.
ax.set_ylabel('Latency (us)')

# Adjust the layout.
plt.tight_layout()

# Display the plot.
# plt.show()
plt.savefig("output_plot.png", bbox_inches='tight', dpi=300)
