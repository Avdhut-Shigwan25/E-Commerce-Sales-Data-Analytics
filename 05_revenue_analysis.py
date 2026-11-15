
import pandas as pd
from pathlib import Path

# 1. Load datasets
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

print("Datasets loaded successfully!")

# 2. Convert purchase date into datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# 3. Select delivered orders
delivered_orders = orders[
    orders["order_status"] == "delivered"
].copy()

# 4. Merge orders and order items
sales = pd.merge(
    delivered_orders[["order_id", "order_purchase_timestamp"]],
    items,
    on="order_id",
    how="inner"
)

# 5. Calculate revenue
product_revenue = sales["price"].sum()
shipping_revenue = sales["freight_value"].sum()
total_revenue = product_revenue + shipping_revenue

# 6. Calculate average order value
total_orders = sales["order_id"].nunique()

average_order_value = product_revenue / total_orders

# 7. Display results
print("\n========== REVENUE ANALYSIS ==========")

print("Total Delivered Orders:", total_orders)

print("Product Revenue: R$", round(product_revenue, 2))

print("Shipping Charges: R$", round(shipping_revenue, 2))

print("Total Including Shipping: R$", round(total_revenue, 2))

print("Average Order Value: R$", round(average_order_value, 2))

# 8. Monthly revenue analysis
sales["month"] = (
    sales["order_purchase_timestamp"].dt.to_period("M")
)

monthly_revenue = sales.groupby("month").agg(
    revenue=("price", "sum"),
    orders=("order_id", "nunique")
).reset_index()

monthly_revenue["month"] = monthly_revenue["month"].astype(str)

print("\n========== MONTHLY REVENUE ==========")
print(monthly_revenue.to_string(index=False))

# 9. Find highest revenue month
highest_month = monthly_revenue.loc[
    monthly_revenue["revenue"].idxmax()
]

print("\nHighest Revenue Month:", highest_month["month"])
print("Highest Monthly Revenue: R$", round(highest_month["revenue"], 2))

# 10. Save results
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

monthly_revenue.to_csv(
    output_folder / "monthly_revenue.csv",
    index=False
)

sales.to_csv(
    output_folder / "delivered_sales.csv",
    index=False
)

print("\nRevenue analysis completed successfully!")
