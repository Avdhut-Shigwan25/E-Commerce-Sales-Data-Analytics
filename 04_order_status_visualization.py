
import pandas as pd
import matplotlib.pyplot as plt

# Load order status analysis
data = pd.read_csv(
    "data/processed/order_status_analysis.csv"
)

# Sort data by order count
data = data.sort_values(
    by="order_count",
    ascending=False
)

# Create bar chart
plt.figure(figsize=(11, 6))

plt.bar(
    data["order_status"],
    data["order_count"]
)

plt.title("Olist E-Commerce Order Status Analysis")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.xticks(rotation=30)
plt.tight_layout()

# Save chart
plt.savefig(
    "data/processed/order_status_chart.png",
    dpi=300
)

plt.show()

print("Order status chart generated successfully!")

# Create Pie Chart
plt.figure(figsize=(9, 7))

plt.pie(
    data["order_count"],
    labels=data["order_status"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Order Status Percentage Distribution")

plt.tight_layout()

plt.savefig(
    "data/processed/order_status_pie_chart.png",
    dpi=300
)

plt.show()

print("Pie chart generated successfully!")
