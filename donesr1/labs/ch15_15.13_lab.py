import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read two CSV filenames
file1 = input()
file2 = input()

# Step 2: Load CSV files into DataFrames
df_july = pd.read_csv(file1)
df_dec = pd.read_csv(file2)

# Step 3: Print each DataFrame separately
print(df_july)
print(df_dec)

# Step 4: Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

# July subplot (left)
axes[0].scatter(df_july["Gross Potential"], df_july["Capacity"])
axes[0].set_title("July 2002")
axes[0].set_xlabel("Gross Potential")
axes[0].set_ylabel("Capacity")

# December subplot (right)
axes[1].scatter(df_dec["Gross Potential"], df_dec["Capacity"])
axes[1].set_title("December 2002")
axes[1].set_xlabel("Gross Potential")
axes[1].set_ylabel("Capacity")

# Main title
fig.suptitle("Capacity vs. Gross Potential")

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle

# Step 5: Save the figure
plt.savefig(
