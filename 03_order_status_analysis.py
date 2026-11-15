
import pandas as pd

# Load the orders dataset
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

print("========== ORDER STATUS ANALYSIS ==========")

# Count orders by status
status_count = orders["order_status"].value_counts()

print("\n1. Orders by Status:")
print(status_count)

# Calculate percentage
status_percentage = (
    orders["order_status"].value_counts(normalize=True) * 100
)

print("\n2. Order Status Percentage:")
print(status_percentage.round(2))

# Total orders
total_orders = len(orders)

print("\n3. Total Orders:", total_orders)

# Delivered orders
delivered = (orders["order_status"] == "delivered").sum()

print("4. Delivered Orders:", delivered)

# Cancelled orders
cancelled = (orders["order_status"] == "canceled").sum()

print("5. Cancelled Orders:", cancelled)

# Delivery rate
delivery_rate = (delivered / total_orders) * 100

print("6. Delivery Rate:", round(delivery_rate, 2), "%")

# Save results
summary = pd.DataFrame({
    "order_status": status_count.index,
    "order_count": status_count.values,
    "percentage": status_percentage.values
})

summary.to_csv(
    "data/processed/order_status_analysis.csv",
    index=False
)

print("\n7. Analysis saved successfully!")
