WITH year_orders AS (
    SELECT customer_id, order_id
    FROM orders
    WHERE order_date BETWEEN '2040-01-01' AND '2040-12-31'
),
customer_totals AS (
    SELECT 
        yo.customer_id,
        SUM(oi.quantity * oi.unit_price) AS total_spent_in_year,
        COUNT(DISTINCT yo.order_id) AS orders_in_year
    FROM year_orders yo
    JOIN order_items oi ON yo.order_id = oi.order_id
    GROUP BY yo.customer_id
)
SELECT 
    c.customer_id, 
    c.customer_name, 
    ct.total_spent_in_year,
    ct.orders_in_year
FROM 
    customers c
JOIN 
    customer_totals ct ON c.customer_id = ct.customer_id
ORDER BY 
    ct.total_spent_in_year DESC;
