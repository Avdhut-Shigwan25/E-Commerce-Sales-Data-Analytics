import pandas as pd

print("Starting Data Analysis...")

file_path = "data/raw/olist_orders_dataset.csv"

orders = pd.read_csv(file_path)

print("\nDataset loaded successfully!")

print("\nFirst 5 records:")
print(orders.head())

print("\nDataset shape:")
print(orders.shape)

print("\nColumn names:")
print(orders.columns.tolist())

print("\nMissing values:")
print(orders.isnull().sum())

print("\nDuplicate records:")
print(orders.duplicated().sum())

print("\nOrder status:")
print(orders["order_status"].value_counts())

print("\nAnalysis completed!")