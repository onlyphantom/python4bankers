SELECT 
    purpose, 
    MAX(CAST(loan_amount AS integer)) AS MaxDisbursed
FROM records
GROUP BY purpose
ORDER BY MaxDisbursed DESC;

SELECT 
    purpose, 
    loan_condition,
    AVG(CAST(loan_amount AS integer)) AS AvgPrincipal,
    AVG(CAST(interest_rate AS decimal)) AS AvgInterest
FROM records
WHERE income_category = "Low"
GROUP BY purpose, loan_condition
ORDER BY purpose;