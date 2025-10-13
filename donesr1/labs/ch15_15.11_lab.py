import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file from input
filename = input()

# Step 2: Read the CSV into a DataFrame
df = pd.read_csv(filename)

# Step 3: Calculate averages and print
avg_delayed = df["Delayed"].mean()
avg_cancelled = df["Cancelled"].mean()

print(f"Average delays: {avg_delayed:.2f}")
print(f"Average cancellations: {avg_cancelled:.2f}")

# Step 4: Plot Delays and Cancellations
plt.plot(df["Month"], df["Delayed"], label="Delays")
plt.plot(df["Month"], df["Cancelled"], label="Cancellations")

# Step 5: Add labels, title, and legend
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight status at LAX", fontsize=14)
plt.legend()

# Step 6: Save the figure
plt.savefig("output_fig.png")
