# Write your MySQL query statement below
SELECT w.id FROM Weather w
INNER JOIN Weather p 
ON w.recordDate=date_add(p.recordDate,interval 1 day)
and w.temperature>p.temperature;