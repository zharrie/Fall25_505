import matplotlib.pyplot as plt
import pandas as pd

file1 = input()
file2 = input()

# TODO: Read in .csv files as dataframes
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# TODO: Print each dataframe individually
print(df1)
print(df2)

# TODO: Create plots for both July and December in one image
fig, (ax1, ax2) = plt.subplots(1, 2)

# Left subplot - July
ax1.scatter(df1["Gross Potential"], df1["Capacity"])
ax1.set_title("July 2002")
ax1.set_xlabel("Gross Potential")
ax1.set_ylabel("Capacity")

# Right subplot - December
ax2.scatter(df2["Gross Potential"], df2["Capacity"])
ax2.set_title("December 2002")
ax2.set_xlabel("Gross Potential")
ax2.set_ylabel("Capacity")

# Main title
fig.suptitle("Capacity vs. Gross Potential")

plt.savefig("subplots.png")
