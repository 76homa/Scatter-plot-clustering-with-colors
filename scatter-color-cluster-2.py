import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap

# Sample data
file_path = "C:/Users/homa.behmardi/Downloads/24 - 4G Sector Trend database-Daily Report_ 16 Mordad - 15 Shahrivar.xlsx"
data = pd.read_excel(file_path, sheet_name="Report")

# Extract the relevant columns from your DataFrame
connected_users_of_days = data["connected users of days"]
throughput = data["Average  DL Thr Mbps"]
average_dl_prb = data["Average DL PRB"]

# Create a colormap for different PRB values
cmap = ListedColormap(['blue', 'green', 'red'])  # You can customize the colors

# Create a scatter plot with different colors based on PRB values
plt.scatter(
    connected_users_of_days,
    throughput,
    c=average_dl_prb,  # Use PRB values for coloring
    cmap=cmap,
    marker='o',
    label='Average DL PRB',
)

# Set labels and legend
plt.xlabel('Connected Users of Days')
plt.ylabel('Average DL Thr Mbps')
plt.legend()

# Add color bar to show the mapping between colors and PRB values
plt.colorbar(label='Average DL PRB')

# Show the plot
plt.grid(True)
plt.title('Scatter Plot with Different Colors Based on DL PRB')
plt.show()
