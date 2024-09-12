SELECT 
    customers.customer_id, 
    customers.customer_name, 
    (SELECT COUNT(*) FROM orders WHERE orders.customer_id = customers.customer_id) AS total_orders,
    (SELECT SUM(order_items.quantity * order_items.unit_price) 
     FROM order_items 
     JOIN orders ON order_items.order_id = orders.order_id 
     WHERE orders.customer_id = customers.customer_id) AS total_spent
FROM 
    customers
WHERE 
    customers.customer_name LIKE '%Kesha%'
ORDER BY 
    total_spent DESC;
