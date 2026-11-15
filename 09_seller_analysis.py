
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")

print("\n========== SELLER ANALYSIS ==========")

# Merge order items with seller information
df = items.merge(sellers, on="seller_id", how="left")

# Total sellers
print("\nTotal Registered Sellers:", sellers["seller_id"].nunique())

# Seller revenue analysis
seller_analysis = df.groupby("seller_id").agg(
    total_orders=("order_id", "nunique"),
    total_revenue=("price", "sum")
).sort_values("total_revenue", ascending=False)

# Top 10 sellers by revenue
top_sellers = seller_analysis.head(10)

print("\nTop 10 Sellers by Revenue:")
print(top_sellers.round(2))

# Average seller revenue
print("\nAverage Revenue Per Seller:",
      round(seller_analysis["total_revenue"].mean(), 2))

# Top 10 sellers chart
plt.figure(figsize=(12, 6))

top_sellers["total_revenue"].plot(kind="bar")

plt.title("Top 10 Sellers by Revenue")
plt.xlabel("Seller ID")
plt.ylabel("Revenue (R$)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("reports/top_sellers.png")
plt.show()

print("\nSeller Analysis Completed Successfully!")
