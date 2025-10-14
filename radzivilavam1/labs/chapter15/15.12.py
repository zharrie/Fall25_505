import matplotlib.pyplot as plt
import pandas as pd

file = input()

# TODO: Read in CSV file as a dataframe
df = pd.read_csv(file)

# TODO: Insert a column to the dataframe as the last column
#       Label the column "Size", which contains half the values in column "Gross Potential"
df["Size"] = df["Gross Potential"] / 2

# TODO: Output dataframe
print(df)

# TODO: Create scatter plot
plt.scatter(df["Capacity"], df["Gross Potential"], marker="x", color="orange", s=df["Size"])

# TODO: Add axis labels and title
plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)

# TODO: Add gridlines
plt.grid(True, linestyle="--")

# TODO: Save figure as output_fig.png
plt.savefig("output_fig.png")
