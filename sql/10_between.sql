-- the inner subquery should not have a semi colon
SELECT * 
FROM records 
WHERE region IN (
    SELECT region
    FROM records
    GROUP BY region
    HAVING COUNT(region) BETWEEN 200000 AND 210000
) AND
    CAST(loan_amount AS integer) BETWEEN 15000 AND 35000   
LIMIT 20;
