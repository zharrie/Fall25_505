import matplotlib.pyplot as plt
import pandas as pd

file1 = input()
file2 = input()

#Read in .csv files as dataframes
df_july = pd.read_csv(file1)
df_dec = pd.read_csv(file2)

#Print each dataframe individually
print(df_july)
print(df_dec)

#Create a figure with two scatter subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Capacity vs Gross Potential", fontsize=16)

#Left subplot: July
axes[0].scatter(df_july["Gross Potential"], df_july["Capacity"], color="blue", marker="o")
axes[0].set_xlabel("Gross Potential")
axes[0].set_ylabel("Capacity")
axes[0].set_title(f"July {df_july['Year'].iloc[0]}")

#Right subplot: December
axes[1].scatter(df_dec["Gross Potential"], df_dec["Capacity"], color="green", marker="x")
axes[1].set_xlabel("Gross Potential")
axes[1].set_ylabel("Capacity")
axes[1].set_title(f"December {df_dec['Year'].iloc[0]}")

plt.savefig("subplots.png")
