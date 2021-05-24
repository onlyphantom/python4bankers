SELECT region, COUNT(region) AS total
FROM records
GROUP BY region
HAVING total > 200000;

SELECT 
    purpose, 
    loan_condition,
    AVG(CAST(loan_amount AS integer)) AS AvgPrincipal,
    AVG(CAST(interest_rate AS decimal)) AS AvgInterest
FROM records
WHERE income_category = "Low"
GROUP BY purpose, loan_condition
HAVING AvgPrincipal > 10000
ORDER BY purpose;