# Write your MySQL query statement below
SELECT *,IF(((z<x+y) AND (x<y+z) AND (y<x+z)),'Yes','No') AS triangle FROM Triangle;