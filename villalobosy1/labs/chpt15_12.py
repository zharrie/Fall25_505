import matplotlib.pyplot as plt
import pandas as pd

file = input()

df = pd.read_csv(file)

df["Size"] = df["Gross Potential"] / 2

print(df)

plt.scatter(
    x=df["Capacity"],
    y=df["Gross Potential"],
    marker='x',
    color='orange',
    s=df["Size"]
)

plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)

plt.grid(linestyle='--')

plt.savefig("output_fig.png")