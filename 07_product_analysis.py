
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
categories = pd.read_csv(
    "data/raw/product_category_name_translation.csv"
)

# Merge datasets
df = items.merge(products, on="product_id", how="left")
df = df.merge(
    categories,
    on="product_category_name",
    how="left"
)

# Category name in English
df["category"] = df["product_category_name_english"].fillna(
    "Unknown"
)

# Product category analysis
category_analysis = df.groupby("category").agg(
    total_products=("product_id", "count"),
    total_revenue=("price", "sum")
).sort_values("total_revenue", ascending=False)

print("\n========== PRODUCT CATEGORY ANALYSIS ==========")

print("\nTop 10 Categories by Revenue:")
print(category_analysis.head(10).round(2))

# Highest revenue category
print("\nHighest Revenue Category:")
print(category_analysis.index[0])

print("\nHighest Category Revenue:")
print(round(category_analysis.iloc[0]["total_revenue"], 2))

# Plot chart
top_categories = category_analysis.head(10)

plt.figure(figsize=(12, 6))
top_categories["total_revenue"].plot(kind="bar")

plt.title("Top 10 Product Categories by Revenue")
plt.xlabel("Product Category")
plt.ylabel("Revenue (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("reports/top_product_categories.png")
plt.show()

print("\nProduct Analysis Completed Successfully!")
