import matplotlib.pyplot as plt
import pandas as pd

file = input()

#Read in CSV file as a dataframe
df = pd.read_csv(file)

# Insert a new column "Size" at the end, containing half the values of "Gross Potential"
df["Size"] = df["Gross Potential"] / 2

#Output dataframe
print(df)

#Create scatter plot
plt.figure(figsize = (8,5))
plt.scatter(df["Capacity"], df["Gross Potential"], s=df["Size"], marker= "x", color="orange")

#Add axis labels and title
plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)

#Add gridlines
plt.grid(linestyle = "--")

#Save figure as output_fig.png
plt.savefig("output_fig.png")
