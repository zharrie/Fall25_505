import matplotlib.pyplot as plt
import pandas as pd

file1 = input()
file2 = input()

df_july = pd.read_csv(file1)
df_dec = pd.read_csv(file2)

print(df_july)
print(df_dec)

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12, 6))
ax1.scatter(df_july["Gross Potential"], df_july["Capacity"])
ax1.set_title("July 2002")
ax1.set_xlabel("Gross Potential")
ax1.set_ylabel("Capacity")

ax2.scatter(df_dec["Gross Potential"], df_dec["Capacity"])
ax2.set_title("December 2002")
ax2.set_xlabel("Gross Potential")
ax2.set_ylabel("Capacity")

fig.suptitle("Capacity vs. Gross Potential")
plt.savefig("subplots.png")