
-- notice its COUNT, not LENGTH
SELECT purpose, COUNT(purpose) AS frequency
FROM records
GROUP BY purpose
ORDER BY frequency DESC;

-- COUNT, MIN, MAX, SUM, AVG
SELECT purpose, term, AVG(loan_amount) AS AvgAmount
FROM records
GROUP BY purpose, term
ORDER BY term;