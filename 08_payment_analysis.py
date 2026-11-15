
import pandas as pd
import matplotlib.pyplot as plt

# Load payment dataset
payments = pd.read_csv(
    "data/raw/olist_order_payments_dataset.csv"
)

print("\n========== PAYMENT ANALYSIS ==========")

# 1. Total payment records
print("\nTotal Payment Records:", len(payments))

# 2. Payment method analysis
payment_analysis = payments.groupby(
    "payment_type"
).agg(
    transactions=("payment_value", "count"),
    total_revenue=("payment_value", "sum"),
    average_payment=("payment_value", "mean")
).sort_values("total_revenue", ascending=False)

print("\nPayment Method Analysis:")
print(payment_analysis.round(2))

# 3. Most popular payment method
popular_method = payments["payment_type"].value_counts().idxmax()

print("\nMost Popular Payment Method:", popular_method)

# 4. Installment analysis
print("\nAverage Installments:",
      round(payments["payment_installments"].mean(), 2))

# 5. Payment method chart
plt.figure(figsize=(10, 5))

payment_analysis["total_revenue"].plot(kind="bar")

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue (R$)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("reports/payment_analysis.png")
plt.show()

print("\nPayment Analysis Completed Successfully!")
