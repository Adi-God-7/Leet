SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING count(distinct(c.product_key)) = (SELECT count(distinct p.product_key) FROM Product p )