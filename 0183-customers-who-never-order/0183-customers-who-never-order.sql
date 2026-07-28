# Write your MySQL query statement below
SELECT c.name as Customers from 
Customers c LEFT OUTER JOIN Orders o
ON c.id=o.customerId WHERE o.id is NULL