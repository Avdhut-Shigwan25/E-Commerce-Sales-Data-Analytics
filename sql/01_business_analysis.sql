-- ============================================================
-- E-COMMERCE DATA ANALYTICS PROJECT
-- Database: ecommerce_analytics
-- File: 01_business_analysis.sql
-- Purpose: Business analysis using the Olist e-commerce dataset
--
-- Instructions:
-- 1. Open this file in VS Code.
-- 2. Run each analysis query separately in MySQL Command Line Client.
-- 3. Each query ends with a semicolon (;).
-- ============================================================

USE ecommerce_analytics;


-- ============================================================
-- ANALYSIS 1: ORDER STATUS ANALYSIS
-- Shows the number and percentage of orders in each status.
-- ============================================================

SELECT
    order_status,
    COUNT(*) AS total_orders,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM olist_orders),
        2
    ) AS percentage
FROM olist_orders
GROUP BY order_status
ORDER BY total_orders DESC;


-- ============================================================
-- ANALYSIS 2: MONTHLY REVENUE ANALYSIS
-- Calculates monthly product revenue for delivered orders.
-- Shipping charges are excluded.
-- ============================================================

SELECT
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
    ROUND(SUM(oi.price), 2) AS monthly_revenue
FROM olist_orders o
JOIN olist_order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
ORDER BY month;


-- ============================================================
-- ANALYSIS 3: TOP 10 PRODUCT CATEGORIES BY REVENUE
-- Uses the English category translation table.
-- Categories without an English translation are not included.
-- ============================================================

SELECT
    t.product_category_name_english AS product_category,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM olist_order_items oi
JOIN olist_orders o
    ON oi.order_id = o.order_id
JOIN olist_products p
    ON oi.product_id = p.product_id
JOIN product_category_translation t
    ON TRIM(p.product_category_name) = TRIM(t.product_category_name)
WHERE o.order_status = 'delivered'
GROUP BY t.product_category_name_english
ORDER BY total_revenue DESC
LIMIT 10;


-- ============================================================
-- ANALYSIS 4: TOP 10 SELLERS BY REVENUE
-- Shows seller location, product revenue, and distinct orders.
-- Shipping charges are excluded.
-- ============================================================

SELECT
    s.seller_id,
    s.seller_city,
    s.seller_state,
    ROUND(SUM(oi.price), 2) AS total_revenue,
    COUNT(DISTINCT oi.order_id) AS total_orders
FROM olist_sellers s
JOIN olist_order_items oi
    ON s.seller_id = oi.seller_id
JOIN olist_orders o
    ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY
    s.seller_id,
    s.seller_city,
    s.seller_state
ORDER BY total_revenue DESC
LIMIT 10;


-- ============================================================
-- ANALYSIS 5: TOP 10 CUSTOMER STATES
-- Counts unique customers using customer_unique_id.
-- ============================================================

SELECT
    customer_state,
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM olist_customers
GROUP BY customer_state
ORDER BY total_customers DESC
LIMIT 10;


-- ============================================================
-- ANALYSIS 6: PAYMENT METHOD ANALYSIS
-- Counts payment records and summarizes payment value
-- and average installments for each payment type.
-- COUNT(*) represents payment records, not unique orders.
-- ============================================================

SELECT
    payment_type,
    COUNT(*) AS total_payment_records,
    ROUND(SUM(payment_value), 2) AS total_revenue,
    ROUND(AVG(payment_installments), 2) AS average_installments
FROM olist_order_payments
GROUP BY payment_type
ORDER BY total_revenue DESC;


-- ============================================================
-- ANALYSIS 7: AVERAGE ORDER VALUE (AOV)
-- First calculates product value for each delivered order,
-- then calculates the average of those order values.
-- Shipping charges are excluded.
-- ============================================================

SELECT
    COUNT(*) AS total_orders,
    ROUND(SUM(order_value), 2) AS total_product_revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM (
    SELECT
        o.order_id,
        SUM(oi.price) AS order_value
    FROM olist_orders o
    JOIN olist_order_items oi
        ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY o.order_id
) AS order_totals;


-- ============================================================
-- ANALYSIS 8: DELIVERY PERFORMANCE
-- Calculates average delivery time and average days early
-- relative to the estimated delivery date.
-- on_time_deliveries counts deliveries on or before estimate.
-- ============================================================

SELECT
    COUNT(*) AS total_delivered_orders,
    ROUND(
        AVG(
            DATEDIFF(
                order_delivered_customer_date,
                order_purchase_timestamp
            )
        ), 2
    ) AS average_delivery_days,
    ROUND(
        AVG(
            DATEDIFF(
                order_estimated_delivery_date,
                order_delivered_customer_date
            )
        ), 2
    ) AS average_days_before_estimated_date,
    SUM(
        CASE
            WHEN order_delivered_customer_date <= order_estimated_delivery_date
            THEN 1
            ELSE 0
        END
    ) AS on_time_deliveries
FROM olist_orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL;


-- ============================================================
-- END OF BUSINESS ANALYSIS QUERIES
-- ============================================================
