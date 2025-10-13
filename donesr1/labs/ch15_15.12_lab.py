import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file name
filename = input()

# Step 2: Load the CSV into a DataFrame
df = pd.read_csv(filename)

# Step 3: Add 'Size' column at the end
df["Size"] = df["Gross Potential"] / 2

# Step 4: Output the DataFrame
print(df)

# Step 5: Create scatter plot
plt.scatter(df["Capacity"], df["Gross Potential"],
            marker='x', color='orange', s=df["Size"])

# Step 6: Add labels, title, and grid
plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)
plt.grid(linestyle='--')

# Step 7: Save the figure
plt.savefig("output_fig.png")
