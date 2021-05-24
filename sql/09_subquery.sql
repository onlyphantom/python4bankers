-- the inner subquery should not have a semi colon
SELECT * 
FROM records 
WHERE region IN (
    SELECT region
    FROM records
    GROUP BY region
    HAVING COUNT(region) > 200000
)
LIMIT 20;
