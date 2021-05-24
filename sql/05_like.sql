-- SQLite provides two wildcards for constructing patterns. They are percent sign % and underscore _ :

-- `%` wildcard matches any sequence of zero or more characters.
-- `_` wildcard matches any single character.
-- `b%` matches `bank`, `bytes`, `bit`
-- `%ion` matches `institution`, `renovation`
-- `%it% matches any string containing `it`

-- `b_nk` matches `bank`, `bunk`
-- `l__n` matches `loan`, `lean`

-- "A" LIKE "a" is true (non case sensitive)
-- to set case-sensitive: PRAGMA case_sensitive_like = true;

SELECT issue_d, region, purpose
FROM records
WHERE purpose LIKE '%business'
ORDER BY purpose
LIMIT 10;

SELECT *
FROM records
WHERE 
    purpose LIKE '%business'
    AND term LIKE '%36%'
ORDER BY purpose
LIMIT 10;