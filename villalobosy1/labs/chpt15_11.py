import pandas as pd
import matplotlib.pyplot as plt


file = input()


df = pd.read_csv(file)

avg_delayed = df["Delayed"].mean()
avg_cancelled = df["Cancelled"].mean()

print(f"Average delays: {avg_delayed:.2f}")
print(f"Average cancellations: {avg_cancelled:.2f}")

plt.plot(df["Month"], df["Delayed"], label = "Delays")
plt.plot(df["Month"], df["Cancelled"], label="Cancellations")

plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight status at LAX", fontsize=14)
plt.legend()
plt.savefig("output_fig.png")
