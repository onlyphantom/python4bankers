SELECT issue_d, term, term_category
FROM records
WHERE term_category = 2
LIMIT 10;

SELECT issue_d, region, purpose
FROM records
WHERE purpose = 'debt_consolidation'
ORDER BY purpose
LIMIT 10;

SELECT issue_d, region, purpose
FROM records
WHERE purpose IN ('small_business', 'debt_consolidation', 'credit_card', 'major_purchase')
ORDER BY region
LIMIT 10;

SELECT issue_d, purpose, grade, loan_amount
FROM records
WHERE grade NOT IN ('A', 'B') OR loan_condition = 'Bad Loan'
LIMIT 10;