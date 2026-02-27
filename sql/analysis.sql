-- ============================================================
-- PROJECT: Inventory Management & Supply Chain Analysis
-- Author : Deepak Dwivedi
-- Tools  : MySQL + Excel + Power BI
-- Dataset: Supply Chain Analysis Dataset
-- ============================================================

-- ── SETUP ────────────────────────────────────────────────────
CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

CREATE TABLE IF NOT EXISTS supply_chain (
    product_type            VARCHAR(50),
    sku                     VARCHAR(20),
    price                   DECIMAL(10,2),
    availability            INT,
    number_of_products_sold INT,
    revenue_generated       DECIMAL(12,2),
    customer_demographics   VARCHAR(30),
    stock_levels            INT,
    lead_times              INT,
    order_quantities        INT,
    shipping_times          INT,
    shipping_carriers       VARCHAR(30),
    shipping_costs          DECIMAL(10,2),
    supplier_name           VARCHAR(50),
    location                VARCHAR(50),
    lead_time               INT,
    production_volumes      INT,
    manufacturing_lead_time INT,
    manufacturing_costs     DECIMAL(10,2),
    inspection_results      VARCHAR(20),
    defect_rates            DECIMAL(5,4),
    transportation_modes    VARCHAR(30),
    routes                  VARCHAR(50),
    costs                   DECIMAL(10,2)
);

-- NOTE: Import CSV via MySQL Workbench Table Import Wizard


-- ============================================================
-- ANALYSIS 1: Inventory Overview KPIs
-- ============================================================
SELECT
    COUNT(DISTINCT sku)                             AS total_skus,
    SUM(stock_levels)                               AS total_stock_units,
    ROUND(SUM(revenue_generated), 2)                AS total_revenue,
    SUM(number_of_products_sold)                    AS total_units_sold,
    ROUND(AVG(defect_rates) * 100, 2)               AS avg_defect_rate_pct,
    ROUND(AVG(lead_times), 1)                       AS avg_lead_time_days,
    ROUND(SUM(manufacturing_costs), 2)              AS total_manufacturing_cost
FROM supply_chain;


-- ============================================================
-- ANALYSIS 2: Revenue & Profit by Product Type
-- ============================================================
SELECT
    product_type,
    COUNT(DISTINCT sku)                             AS total_skus,
    SUM(number_of_products_sold)                    AS units_sold,
    ROUND(SUM(revenue_generated), 2)                AS total_revenue,
    ROUND(SUM(manufacturing_costs), 2)              AS total_cost,
    ROUND(SUM(revenue_generated) - SUM(manufacturing_costs), 2) AS gross_profit,
    ROUND((SUM(revenue_generated) - SUM(manufacturing_costs))
          / SUM(revenue_generated) * 100, 2)        AS profit_margin_pct
FROM supply_chain
GROUP BY product_type
ORDER BY total_revenue DESC;


-- ============================================================
-- ANALYSIS 3: ABC Inventory Classification
-- A = High Value (top 70% revenue)
-- B = Medium Value (next 20%)
-- C = Low Value (bottom 10%)
-- ============================================================
WITH revenue_ranked AS (
    SELECT
        sku,
        product_type,
        stock_levels,
        number_of_products_sold,
        revenue_generated,
        SUM(revenue_generated) OVER ()              AS total_revenue,
        SUM(revenue_generated) OVER (ORDER BY revenue_generated DESC)
                                                    AS running_total
    FROM supply_chain
),
abc_classified AS (
    SELECT
        sku,
        product_type,
        stock_levels,
        revenue_generated,
        ROUND(running_total / total_revenue * 100, 2) AS cumulative_pct,
        CASE
            WHEN running_total / total_revenue <= 0.70 THEN 'A - High Value'
            WHEN running_total / total_revenue <= 0.90 THEN 'B - Medium Value'
            ELSE 'C - Low Value'
        END AS abc_category
    FROM revenue_ranked
)
SELECT
    abc_category,
    COUNT(sku)                                      AS sku_count,
    ROUND(SUM(revenue_generated), 2)                AS total_revenue,
    SUM(stock_levels)                               AS total_stock
FROM abc_classified
GROUP BY abc_category
ORDER BY abc_category;


-- ============================================================
-- ANALYSIS 4: Slow-Moving Inventory Detection
-- Low sales + high stock = cash tied up
-- ============================================================
SELECT
    sku,
    product_type,
    stock_levels,
    number_of_products_sold,
    ROUND(revenue_generated, 2)                     AS revenue,
    CASE
        WHEN stock_levels > 0
        THEN ROUND(number_of_products_sold / stock_levels * 100, 1)
        ELSE 0
    END                                             AS sell_through_rate_pct,
    CASE
        WHEN number_of_products_sold / NULLIF(stock_levels, 0) < 0.2
            THEN '🔴 Slow Moving — Review'
        WHEN number_of_products_sold / NULLIF(stock_levels, 0) < 0.5
            THEN '🟡 Below Average'
        ELSE '🟢 Healthy'
    END                                             AS inventory_health
FROM supply_chain
ORDER BY sell_through_rate_pct ASC
LIMIT 20;


-- ============================================================
-- ANALYSIS 5: Supplier Performance Scorecard
-- ============================================================
SELECT
    supplier_name,
    COUNT(DISTINCT sku)                             AS products_supplied,
    ROUND(AVG(lead_times), 1)                       AS avg_lead_time_days,
    ROUND(AVG(defect_rates) * 100, 2)               AS avg_defect_rate_pct,
    ROUND(SUM(manufacturing_costs), 2)              AS total_cost,
    ROUND(SUM(revenue_generated), 2)                AS revenue_generated,
    CASE
        WHEN AVG(defect_rates) > 0.05 THEN '🔴 Poor Quality'
        WHEN AVG(defect_rates) > 0.02 THEN '🟡 Average'
        ELSE '🟢 Good Quality'
    END                                             AS quality_rating,
    CASE
        WHEN AVG(lead_times) > 20 THEN '🔴 Slow'
        WHEN AVG(lead_times) > 12 THEN '🟡 Average'
        ELSE '🟢 Fast'
    END                                             AS speed_rating
FROM supply_chain
GROUP BY supplier_name
ORDER BY avg_defect_rate_pct ASC;


-- ============================================================
-- ANALYSIS 6: Stockout Risk Analysis
-- Low stock vs high sales velocity = stockout risk
-- ============================================================
SELECT
    sku,
    product_type,
    supplier_name,
    stock_levels,
    number_of_products_sold,
    lead_times,
    ROUND(number_of_products_sold / 30.0, 1)        AS daily_sales_rate,
    ROUND(stock_levels / NULLIF(number_of_products_sold / 30.0, 0), 0)
                                                    AS days_of_stock_remaining,
    CASE
        WHEN stock_levels / NULLIF(number_of_products_sold / 30.0, 0) < lead_times
            THEN '🚨 STOCKOUT RISK — Reorder Now'
        WHEN stock_levels / NULLIF(number_of_products_sold / 30.0, 0) < lead_times * 1.5
            THEN '⚠️  Low Stock — Monitor'
        ELSE '✅ Adequate Stock'
    END                                             AS stock_status
FROM supply_chain
ORDER BY days_of_stock_remaining ASC
LIMIT 20;


-- ============================================================
-- ANALYSIS 7: Shipping Cost vs Mode Analysis
-- ============================================================
SELECT
    transportation_modes,
    shipping_carriers,
    COUNT(sku)                                      AS shipments,
    ROUND(AVG(shipping_costs), 2)                   AS avg_shipping_cost,
    ROUND(SUM(shipping_costs), 2)                   AS total_shipping_cost,
    ROUND(AVG(shipping_times), 1)                   AS avg_shipping_days,
    ROUND(SUM(revenue_generated), 2)                AS revenue_covered
FROM supply_chain
GROUP BY transportation_modes, shipping_carriers
ORDER BY avg_shipping_cost ASC;


-- ============================================================
-- ANALYSIS 8: Defect Rate by Product Type & Supplier
-- ============================================================
SELECT
    product_type,
    supplier_name,
    COUNT(sku)                                      AS products,
    ROUND(AVG(defect_rates) * 100, 2)               AS avg_defect_pct,
    SUM(CASE WHEN inspection_results = 'Fail' THEN 1 ELSE 0 END) AS failed_inspections,
    ROUND(SUM(manufacturing_costs), 2)              AS total_mfg_cost,
    CASE
        WHEN AVG(defect_rates) > 0.05 THEN '🔴 Action Required'
        WHEN AVG(defect_rates) > 0.02 THEN '🟡 Monitor'
        ELSE '🟢 Acceptable'
    END                                             AS defect_status
FROM supply_chain
GROUP BY product_type, supplier_name
ORDER BY avg_defect_pct DESC;


-- ============================================================
-- ANALYSIS 9: Revenue per Unit vs Stock Efficiency
-- ============================================================
SELECT
    product_type,
    sku,
    price,
    stock_levels,
    number_of_products_sold,
    ROUND(revenue_generated, 2)                     AS revenue,
    ROUND(manufacturing_costs, 2)                   AS mfg_cost,
    ROUND(revenue_generated - manufacturing_costs, 2) AS gross_profit,
    ROUND((revenue_generated - manufacturing_costs)
          / NULLIF(revenue_generated, 0) * 100, 2)  AS margin_pct,
    ROUND(revenue_generated / NULLIF(stock_levels, 0), 2) AS revenue_per_stock_unit
FROM supply_chain
ORDER BY revenue_per_stock_unit DESC
LIMIT 15;


-- ============================================================
-- ANALYSIS 10: Location-wise Performance
-- ============================================================
SELECT
    location,
    COUNT(DISTINCT sku)                             AS products,
    ROUND(SUM(revenue_generated), 2)                AS total_revenue,
    ROUND(SUM(manufacturing_costs), 2)              AS total_cost,
    ROUND(AVG(lead_times), 1)                       AS avg_lead_days,
    ROUND(AVG(defect_rates) * 100, 2)               AS avg_defect_pct,
    ROUND(SUM(revenue_generated) - SUM(manufacturing_costs), 2) AS gross_profit
FROM supply_chain
GROUP BY location
ORDER BY total_revenue DESC;


-- ============================================================
-- ANALYSIS 11: Reorder Point Calculation
-- Standard formula: Reorder Point = (Daily Sales × Lead Time) + Safety Stock
-- ============================================================
SELECT
    sku,
    product_type,
    supplier_name,
    stock_levels                                    AS current_stock,
    lead_times                                      AS supplier_lead_days,
    number_of_products_sold                         AS monthly_sales,
    ROUND(number_of_products_sold / 30.0, 1)        AS daily_sales,
    ROUND((number_of_products_sold / 30.0) * lead_times, 0)
                                                    AS reorder_point,
    ROUND((number_of_products_sold / 30.0) * lead_times * 0.25, 0)
                                                    AS safety_stock,
    CASE
        WHEN stock_levels <= ROUND((number_of_products_sold / 30.0) * lead_times, 0)
            THEN '🚨 ORDER NOW'
        ELSE '✅ OK'
    END                                             AS action_required
FROM supply_chain
ORDER BY action_required DESC, current_stock ASC;


-- ============================================================
-- ANALYSIS 12: Overall Supply Chain Health Score
-- ============================================================
SELECT
    supplier_name,
    ROUND(AVG(defect_rates) * 100, 2)               AS defect_rate_pct,
    ROUND(AVG(lead_times), 1)                       AS avg_lead_days,
    ROUND(AVG(shipping_costs), 2)                   AS avg_ship_cost,
    COUNT(DISTINCT sku)                             AS products,
    ROUND(SUM(revenue_generated), 2)                AS revenue,
    -- Composite score: lower defect (40%) + faster lead (30%) + lower cost (30%)
    ROUND(
        (1 - AVG(defect_rates)) * 40 +
        (1 - (AVG(lead_times) / 30)) * 30 +
        (1 - (AVG(shipping_costs) / 100)) * 30
    , 1)                                            AS supplier_health_score
FROM supply_chain
GROUP BY supplier_name
ORDER BY supplier_health_score DESC;
