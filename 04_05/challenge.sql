SELECT 
    c.customer_id, 
    c.customer_name, 
    (
        SELECT SUM(oi.quantity * oi.unit_price)
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.customer_id = c.customer_id
        AND o.order_id IN (
            SELECT o2.order_id 
            FROM orders o2 
            WHERE o2.order_date >= '2040-01-01'
            AND o2.order_date <= '2040-12-31'
        )
    ) AS total_spent_in_year,
    (
        SELECT COUNT(o3.order_id)
        FROM orders o3
        WHERE o3.customer_id = c.customer_id
        AND o3.order_date >= '2040-01-01'
        AND o3.order_date <= '2040-12-31'
    ) AS orders_in_year
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
WHERE 
    EXISTS (
        SELECT 1
        FROM orders o4
        WHERE o4.customer_id = c.customer_id
        AND o4.order_date >= '2040-01-01'
        AND o4.order_date <= '2040-12-31'
    )
ORDER BY 
    total_spent_in_year DESC;
