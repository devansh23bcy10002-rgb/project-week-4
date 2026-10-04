"""
Week 4 Data Analyst Capstone: Retail Sales Analysis
Run: python analysis.py
Dependencies: pandas, matplotlib
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["order_date"])
print("Raw rows:", len(df))

# Clean: remove duplicate order IDs and fill missing categorical values
df = df.drop_duplicates(subset=["order_id"])
df["region"] = df["region"].fillna("Unknown")
df = df.dropna(subset=["order_date", "product", "units", "unit_price"])
df["revenue"] = df["units"] * df["unit_price"]

# Explore and aggregate
summary = df[["units", "unit_price", "revenue"]].describe()
by_region = df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
by_product = df.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
monthly = df.set_index("order_date").resample("MS")["revenue"].sum().reset_index()

summary.to_csv(OUT / "descriptive_statistics.csv")
by_region.to_csv(OUT / "revenue_by_region.csv", index=False)
by_product.to_csv(OUT / "revenue_by_product.csv", index=False)
monthly.to_csv(OUT / "monthly_revenue.csv", index=False)

plt.figure(figsize=(8, 4.5))
plt.bar(by_region["region"], by_region["revenue"])
plt.title("Revenue by Region")
plt.xlabel("Region"); plt.ylabel("Revenue")
plt.tight_layout(); plt.savefig(OUT / "revenue_by_region.png", dpi=160); plt.close()

plt.figure(figsize=(8, 4.5))
plt.bar(by_product["product"], by_product["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product"); plt.ylabel("Revenue")
plt.xticks(rotation=20); plt.tight_layout()
plt.savefig(OUT / "revenue_by_product.png", dpi=160); plt.close()

plt.figure(figsize=(8, 4.5))
plt.plot(monthly["order_date"], monthly["revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month"); plt.ylabel("Revenue")
plt.tight_layout(); plt.savefig(OUT / "monthly_revenue.png", dpi=160); plt.close()

print("\nTotal revenue:", round(df["revenue"].sum(), 2))
print("\nRevenue by region:\n", by_region.to_string(index=False))
print("\nRevenue by product:\n", by_product.to_string(index=False))
print("\nOutputs saved to:", OUT)
