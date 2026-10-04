# Week 4 Data Analyst Capstone: Retail Sales Analysis

This project demonstrates data cleaning, exploratory analysis, aggregation, charts, and stakeholder recommendations. The included `sales_data.csv` is a **synthetic practice dataset**, not the Google Sheets dataset referenced in the course handout.

## Run
1. Install Python 3.9+.
2. Run `pip install -r requirements.txt`.
3. Run `python analysis.py`.

Generated tables and PNG charts are saved in `outputs/`.

## BI dashboard
Import `sales_data.csv` into Power BI or Tableau. Suggested visuals:
- KPI cards: Total Revenue, Total Units, Number of Orders
- Bar chart: Revenue by Region
- Bar chart: Revenue by Product
- Line chart: Monthly Revenue
- Slicers: Region, Product, Order Date

## SQL example
```sql
SELECT region, SUM(units * unit_price) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;
```

Replace the sample CSV with the official course dataset before submitting if your instructor expects that dataset.
