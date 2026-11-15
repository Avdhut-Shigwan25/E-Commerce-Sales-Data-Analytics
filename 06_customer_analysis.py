
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# Merge customer and order data
df = orders.merge(customers, on="customer_id", how="left")

# 1. Total customers
print("\n========== CUSTOMER ANALYSIS ==========")

print("Total Customer Records:", len(customers))
print("Unique Customers:", customers["customer_unique_id"].nunique())
print("Total Orders:", len(orders))

# 2. Top 10 states
state_counts = customers.groupby("customer_state")[
    "customer_unique_id"
].nunique().sort_values(ascending=False).head(10)

print("\nTop 10 States:")
print(state_counts)

# 3. Top 10 cities
city_counts = customers.groupby("customer_city")[
    "customer_unique_id"
].nunique().sort_values(ascending=False).head(10)

print("\nTop 10 Cities:")
print(city_counts)

# 4. Orders per customer
orders_per_customer = df.groupby(
    "customer_unique_id"
)["order_id"].nunique()

print("\nAverage Orders Per Customer:",
      round(orders_per_customer.mean(), 2))

# 5. State-wise customer chart
plt.figure(figsize=(10, 5))
state_counts.plot(kind="bar")

plt.title("Top 10 States by Customer Count")
plt.xlabel("State")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("reports/top_customer_states.png")
plt.show()

print("\nCustomer Analysis Completed Successfully!")
