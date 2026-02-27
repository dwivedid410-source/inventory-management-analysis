# 📦 Inventory Management & Supply Chain Analysis
### Tools: MySQL · Microsoft Excel · Power BI
### Dataset: Supply Chain Analysis Dataset

---

## 📌 Project Overview

Analyzed end-to-end supply chain data to identify inventory inefficiencies,
supplier performance gaps, and stockout risks. Built an ABC classification
system and reorder point calculator to optimize stock management.

**Business Problem:** The company was experiencing both stockouts (lost sales)
and overstock situations (cash tied up in slow-moving inventory) simultaneously —
indicating poor inventory visibility and no systematic reorder process.

---

## 🔍 Key Business Insights

| # | Insight | Business Impact |
|---|---------|----------------|
| 1 | **23 SKUs** identified as slow-moving with <20% sell-through rate | Free up warehouse space, run clearance |
| 2 | **Supplier C** has 3x higher defect rate than average (7.2% vs 2.1%) | Switch to backup supplier or penalize |
| 3 | **Air shipping** costs 4x road but only saves 3 days on average | Shift 60% of air shipments to road transport |
| 4 | **8 SKUs** are at stockout risk — current stock below reorder point | Immediate purchase orders required |
| 5 | **Category A products** (top 70% revenue) represent only 30% of SKUs | Focus safety stock investment on A-items |

---

## 📊 Dashboard Pages (Power BI)

**Page 1 — Inventory Overview**
- Total SKUs, Stock Units, Revenue KPI cards
- ABC Classification donut chart
- Stock health status by product type
- Revenue vs Cost bar chart

**Page 2 — Stockout & Reorder Monitor**
- Stockout risk traffic light table
- Days of stock remaining bar chart
- Reorder point vs current stock comparison
- Slow-moving inventory list

**Page 3 — Supplier Scorecard**
- Supplier health score ranking
- Defect rate comparison bar chart
- Lead time by supplier
- Shipping cost by transport mode

---

## 🗂️ Project Structure

```
inventory-management-analysis/
├── README.md
├── sql/
│   └── analysis.sql      ← 12 queries including ABC classification & reorder calc
├── data/
│   └── supply_chain.csv  ← Download from Kaggle (link below)
└── powerbi/
    └── dashboard_preview.png
```

---

## 🚀 How to Run This Project

**Step 1 — Get the Dataset**
Download from Kaggle:
https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis

**Step 2 — Load into MySQL**
```sql
CREATE DATABASE inventory_db;
USE inventory_db;
-- Use MySQL Workbench Import Wizard to load CSV
```

**Step 3 — Run Analysis**
Open `sql/analysis.sql` — run queries section by section.

**Step 4 — Power BI Dashboard**
Connect Power BI to MySQL → build 3-page inventory dashboard.

---

## 📈 Excel Analysis Performed

- ABC Classification using PERCENTILE function
- Inventory Turnover Ratio = Sales / Average Stock
- Reorder Point formula: (Daily Sales × Lead Time) + Safety Stock
- Conditional formatting: Red (stockout risk), Green (healthy)
- Supplier scorecard pivot table
- Slow-moving SKU list with sell-through rate

---

## 🛠️ Tools & Skills Demonstrated

| Tool | Usage |
|------|-------|
| **MySQL** | 12 queries — Window Functions, CTEs, CASE WHEN, composite scoring |
| **Excel** | ABC analysis, turnover ratios, reorder formulas, conditional formatting |
| **Power BI** | 3-page dashboard, traffic light visuals, supplier scorecard |

---

## 📂 Dataset Source
- **Name:** Supply Chain Analysis Dataset
- **Source:** Kaggle — https://www.kaggle.com/datasets/harshsingh2209/supply-chain-analysis

---

*Project by Deepak Dwivedi | Data Analyst Portfolio*
*LinkedIn: linkedin.com/in/deepak-dwivedi1k*
*GitHub: github.com/dwivedid410-source*
