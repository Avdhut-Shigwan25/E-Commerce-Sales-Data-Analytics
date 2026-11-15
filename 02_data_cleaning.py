
import pandas as pd
from pathlib import Path

# 1. Define file locations
raw_path = Path("data/raw/olist_orders_dataset.csv")
output_path = Path("data/processed/cleaned_orders.csv")

# 2. Load original dataset
orders = pd.read_csv(raw_path)

print("Original dataset shape:", orders.shape)

# 3. Check missing values
print("\nMissing values before cleaning:")
print(orders.isnull().sum())

# 4. Check duplicate records
print("\nExact duplicate rows:", orders.duplicated().sum())

# 5. Remove exact duplicate rows
orders = orders.drop_duplicates()

# 6. Convert date columns into datetime format
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column], errors="coerce"
    )

# 7. Check duplicate order IDs
print("\nDuplicate order IDs:", orders["order_id"].duplicated().sum())

# 8. Display cleaned dataset information
print("\nCleaned dataset shape:", orders.shape)

print("\nMissing values after cleaning:")
print(orders.isnull().sum())

# 9. Save cleaned dataset
output_path.parent.mkdir(parents=True, exist_ok=True)
orders.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Location:", output_path)
