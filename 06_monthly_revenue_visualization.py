
import pandas as pd
import matplotlib.pyplot as plt

# Load monthly revenue data
data = pd.read_csv(
    "data/processed/monthly_revenue.csv"
)

# Convert month into datetime
data["month"] = pd.to_datetime(data["month"])

# Create complete monthly timeline
data = data.set_index("month")

all_months = pd.date_range(
    start=data.index.min(),
    end=data.index.max(),
    freq="MS"
)

data = data.reindex(all_months, fill_value=0)

# Create line chart
plt.figure(figsize=(13, 6))

plt.plot(
    data.index,
    data["revenue"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Revenue Trend - Olist E-Commerce")
plt.xlabel("Month")
plt.ylabel("Product Revenue (R$)")

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save chart
plt.savefig(
    "data/processed/monthly_revenue_trend.png",
    dpi=300
)

plt.show()

print("Monthly revenue chart generated successfully!")
