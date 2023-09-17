# Scatter-plot-clustering-with-colors
This code shows an scatter plot which clusters based on different colors 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
file_path = "C:/Users/homa.behmardi/Downloads/24 - 4G Sector Trend database-Daily Report_ 16 Mordad - 15 Shahrivar.xlsx"
data = pd.read_excel(file_path, sheet_name="Report")

# Extract the relevant columns from your DataFrame
connected_users_of_days = data["connected users of days"]
throughput = data["Average  DL Thr Mbps"]
average_traffic_gb = data["Average Traffic (GB)"]
average_dl_prb = data["Average DL PRB"]

# Define traffic clusters based on specific ranges
conditions = [
    (average_traffic_gb < 100),
    (average_traffic_gb >= 100) & (average_traffic_gb < 600),
    (average_traffic_gb >= 600)
]

cluster_labels = np.select(conditions, ["< 100", "100 < x < 600", "> 600"])

# Define different colors for each traffic cluster
colors = {'< 100': 'red', '100 < x < 600': 'blue', '> 600': 'green'}

# Create a scatter plot with different colors for each traffic cluster and shapes based on DL PRB
for cluster_label in np.unique(cluster_labels):
    mask_cluster = cluster_labels == cluster_label
    plt.scatter(
        connected_users_of_days[mask_cluster],
        throughput[mask_cluster],
        c=colors[cluster_label],  # Assign a different color for each traffic cluster
        marker='o',  # Use the same marker for all points
        label=f'Traffic Cluster: {cluster_label}',
    )

# Set labels and legend
plt.xlabel('Connected Users of Days')
plt.ylabel('Average DL Thr Mbps')
plt.legend()

# Show the plot
plt.grid(True)
plt.title('Scatter Plot with Different Colors Based on Traffic Clusters')
plt.show()
