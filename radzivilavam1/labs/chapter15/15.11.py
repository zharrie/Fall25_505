import matplotlib.pyplot as plt
import pandas as pd

file = input()

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file)

# Calculate averages
avg_delays = df["Delayed"].mean()
avg_cancellations = df["Cancelled"].mean()

# Output averages with two decimal places
print(f"Average delays: {avg_delays:.2f}")
print(f"Average cancellations: {avg_cancellations:.2f}")

# Create line plots
plt.plot(df["Month"], df["Delayed"], label="Delays")
plt.plot(df["Month"], df["Cancelled"], label="Cancellations")

# Add labels, title, and legend
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight Status at LAX", fontsize=14)
plt.legend()

# Save figure as output_fig.png
plt.savefig("output_fig.png")
