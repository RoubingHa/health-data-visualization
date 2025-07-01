import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("health_data.csv", parse_dates=["Date"])

# Summary statistics
print("Basic Stats:\n", df.describe())

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["HeartRate"], label="Heart Rate (bpm)")
plt.plot(df["Date"], df["Weight"], label="Weight (kg)")
plt.plot(df["Date"], df["GumHealthScore"], label="Gum Health Score")
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Health Data Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("health_plot.png")
plt.show()