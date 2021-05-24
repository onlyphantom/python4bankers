## SQL in 3 hours
This is a 11-part practice that serves as a fast-paced introduction, essentials-only introduction to SQL. It is meant as a follow up to [CSV to SQLite](https://www.youtube.com/watch?v=GlyIpx_VDxo) and [Introduction to SQL](https://www.youtube.com/watch?v=e4zZGc4UZGQ), part of the Python for Bankers series. 

It zooms in on the most common operations in SQL, and makes some omission for SQL features outside of the most-common usage patterns (eg. We all agree dropping or renaming a database isn't all that common, right? Right?)

### Disclaimer
Two disclaimers. 

The first is that the exercises use a single-table database, relating to the financial loan dataset that we've been using up to this point in the workshop. This means we won't be seeing joins operations until later part of the workshop, but this is intended as it keeps your focus on the SQL syntaxes and present a more manageable barrier to entry for absolute beginners. 

The second disclaimer is that its primary audience are working professionals who can't find time to work through a textbook on SQL. The exercise is meant to be completed under 1.5 hours, with guidance from the Lead Instructor or Teaching Assistants.

Finally, for all its flexibility and simplicity, SQLite makes a few trade-offs. Most notably, altering tables [are problematic in SQLite](https://sqlite.org/lang_altertable.html). Here's a quick excerpt from the official website:

> Most SQL database engines store the schema already parsed into various system tables. On those database engines, `ALTER TABLE` merely has to make modifications to the corresponding system tables.
> 
> SQLite is different in that it stores the schema in the sqlite_schema table as the original text of the `CREATE` statements that define the schema. Hence `ALTER TABLE` needs to revise the text of the `CREATE` statement. Doing so can be tricky for certain "creative" schema designs.

For the most part of this exercise, it won't matter too much. The only major practical implication would be when we encounter a numeric column that is stored as text. We will use the `CAST AS` option instead of changing the column type as we may have with other database engines.

### Exercises

#### 1. Renaming using ALTER TABLE and RENAME
Let's start off simple. Create a file and name it `01_rename.sql`. Use `ALTER TABLE <table_name> RENAME COLUMN <existing_name> TO <new_name>` to make alterations to the column named `term_cat`. Rename it to `term_category`. 

In some database editor, you may have to refresh your database view to see this change take effect. You can also use `PRAGMA table_info(records);` to check the schema before and after the change.

#### 2. SELECT, LIMIT and OFFSET
Select `id`, `issue_d`, `term`, and `term_category` from the table and show only the first 10 results.

Add an `OFFSET` clause to get the first 10 rows starting from the 6th row.

#### 3. Return unique values from a column

Use `SELECT DISTINCT <column>` to select only the unique values. 

#### 4. Conditionally return rows using WHERE

Select rows where the purpose of the loan is `debt_consolidation`. Order it by purpose and return the first 10 rows. 

Select rows where the purpose of the loan is one of `small_business`, `debt_consolidation`, `credit_card`, `major_purchase`. Order it by purpose and return the first 10 rows. 

#### 5. Pattern matching using LIKE
SQLite provides two wildcards for constructing patterns. They are percent sign `%` and underscore `_`.

- `%` wildcard matches any sequence of zero or more characters.
- `_` wildcard matches any single character.
- `b%` matches `bank`, `bytes`, `bit`
- `%ion` matches `institution`, `renovation`
- `%it% matches any string containing `it`

- `b_nk` matches `bank`, `bunk`
- `l__n` matches `loan`, `lean`

"A" LIKE "a" is true (non case sensitive) to set case-sensitive: PRAGMA case_sensitive_like = true;

#### 6. Aggregation and GROUP BY
Using `COUNT()`, return the number of rows in each group of `purpose`. Sort the returned values in descending order of the `COUNT()` column.

Using `AVG()`, return the average loan amount for each combination of `purpose` and `term`. Order by the `term` column.

`MIN`, `MAX`, `SUM`, `COUNT`, and `AVG` are the five aggregation functions frequently used with `GROUP BY`.

#### 7. Aggregation and GROUP BY
Since aggregation is commonly applied on numeric columns, this may present a little bit of problem when our columns are in character strings. You may alter the database table and change the column types, or you may use `CAST AS` to cast the column values from character to either `integer` or `decimal`.

This exercise is similar to the one in (6), but this time make sure numeric columns are casted as numeric. 

Return the maximum `loan_amount` for each `purpose` in descending order.

Return the average `loan_amount` and `interest_rate` for each combination of `purpose` and `loan_condition` where `income_category` of the loan applicant is "Low". Order it by the `purpose` column.

#### 8. Using HAVING to filter on groups
`HAVING` has to be used with `GROUP BY`. They act similarly to how `WHERE` works on rows, except `HAVING` filters on the group levels.

Use `GROUP BY` to count the number of loans given to applicants from each `region`, but return only the groups with a total number exceeding 200,000.

Perform exercise (7) again, but this time add `HAVING`after your `GROUP BY` clause with the condition that return only groups with an average `loan_amount` of more than 10,000.

#### 9. Use subquery to nest a SELECT statement under another

Subqueries allow you to put together more complex queries while maintaining some readability. Fundamentally, a subquery is just a nested level of `SELECT` statement. Combine what you wrote in (8) with `IN` and return rows of records where `region` belongs to one of the regions with more than 200,000 records in the table. 

#### 10. Use BETWEEN to test for values within a range

Your SQL statement should be similar to (9). Select records with the following conditions:
- (a): `region` belongs to one of the regions with more than 200,000 but less than 210,000 records in the table. 
- (b): `loan_amount` is between 15,000 and 35,000

Return the first 20 rows matching both (a) and (b) condition.

#### 11. Use `CREATE VIEW` to pack a query into a named object

A view is the result set of a stored query, useful when we want to "store" our query as an object in the database. 

Use `CREATE VIEW <view_name> AS` followed by your `SELECT` statement to create a view containing records from regions that meet the following conditions:
- (a): `region` belongs to one of the regions with more than 200,000 but less than 210,000 records in the table. 
- (b): `loan_amount` is between 15,000 and 35,000

This should be identical to your query in (10). Name this view `keymarket`. Be sure to end your statement with a semicolon (`;`).

Next, select all columns from `keymarket` and return the first 5 rows.

For additional practice, create a view named `badloans` with the columns `loan_amount`, `purpose`, `dti`, `loan_condition` and `grade` where `loan_condition` is 'Bad Loan' and `grade` is one of 'D', 'E' or 'F'. 

Next, return the total number of loan records and the average `dti` (debt-to-income) for each `purpose` using a `GROUP BY`.

Depending on your database editor or application, you may need to refresh the explorer to see your views being created.