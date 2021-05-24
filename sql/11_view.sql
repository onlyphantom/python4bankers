DROP VIEW IF EXISTS keymarket;

CREATE VIEW keymarket
AS
    SELECT id, region, loan_amount
    FROM records 
    WHERE region IN (
        SELECT region
        FROM records
        GROUP BY region
        HAVING COUNT(region) BETWEEN 200000 AND 210000
    ) AND
        CAST(loan_amount AS integer) BETWEEN 15000 AND 35000   
    LIMIT 20;

SELECT * 
FROM keymarket
ORDER BY id
LIMIT 5;

-- DROP VIEW IF EXISTS badloans;
CREATE VIEW IF NOT EXISTS badloans
AS 
    SELECT loan_amount, purpose, dti, loan_condition, grade
    FROM records
    WHERE loan_condition = 'Bad Loan' AND grade IN ('D','E','F');

SELECT purpose, COUNT(purpose), ROUND(AVG(CAST(dti AS decimal)), 2) AS AvgDTI
FROM badloans
GROUP BY purpose
ORDER BY AvgDTI;