# CSV and SQLite

A CSV (comma-separated values) file is a text file that uses a comma to separate values. Each line of the file holds the comma-separated values related to a data record. 

If you have Microsoft Excel installed or have worked in Google Sheets in the past, chances are you've come across a CSV file.

SQLite on the other hand is "an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine". It is open source, free for use for any purpose whether commercial or private. 

# Using SQLite

You can refer to SQLite's [download page](https://www.sqlite.org/download.html) for the download and installation instructions. If you're on Linux, look for specific instructions on your distros. If you're on macOS you may alternatively install it with [Homebrew](https://brew.sh/).

We're using SQLite in our lessons to learn about working with SQL (Structured Query Language) without having to worry about database provisioning (creating a SQL server, setting up authentication and permissions, connecting securely) which is time- and cost-expensive. 

## Loan Records

To help you jumpstart directly into SQL, I've created `loan.db`, using data originally provided as a CSV from LendingClub. This is a SQLite database. To show you how it's performed, I've outlined the steps in the next section.

# CSV to SQLite
1. Once you have SQLite installed, create a database and name it `loan.db`. This should happen in the same directory as where you stored `loan_new.csv` (or whatever file you plan to import into your SQLite database)

    ```bash
    sqlite3 loan.db
    ```

Note that steps from step 2 onwards are performed in the SQLite shell (not your command prompt or terminal).

2. Since `loan.db` doesn't exist, SQLite will automatically create one for you. Once you're in the `sqlite3` shell, set the mode to `csv` and create a table with the name `records` for our loan records:

    ```sql
    .mode csv records
    ```

3. Perform the import by passing in the name of our CSV file and the table (we named it `records` in step 2):

    ```sql
    .import loan_new.csv records
    ```

And... **You're done!** That's it. It's that simple. The following steps are optional checks and made sure everything work as expected as well as examples of some common sqlite operations.

---

4. Perform a quick check by querying for the tables in our database:

    ```sql
    .tables
    ```

    This returns the following table:

    ```sql
    records
    ```

5. Take a look at the schema of our `records` table. This returns the statement that created our `records` table:

    ```sql
    .schema records
    ```

    This returns the following:
    ```sql
    CREATE TABLE records(
    "id" TEXT,
    "year" TEXT,
    "issue_d" TEXT,
    "final_d" TEXT,
    "emp_length_int" TEXT,
    "home_ownership" TEXT,
    "home_ownership_cat" TEXT,
    "income_category" TEXT,
    "annual_inc" TEXT,
    "income_cat" TEXT,
    "loan_amount" TEXT,
    "term" TEXT,
    "term_cat" TEXT,
    "application_type" TEXT,
    "application_type_cat" TEXT,
    "purpose" TEXT,
    "purpose_cat" TEXT,
    "interest_payments" TEXT,
    "interest_payment_cat" TEXT,
    "loan_condition" TEXT,
    "loan_condition_cat" TEXT,
    "interest_rate" TEXT,
    "grade" TEXT,
    "grade_cat" TEXT,
    "dti" TEXT,
    "total_pymnt" TEXT,
    "total_rec_prncp" TEXT,
    "recoveries" TEXT,
    "installment" TEXT,
    "region" TEXT
    );
    ```

6. You can optionally use `table_info` to get a summary of the table structure (this is more advanced):

    ```sql
    .header on
    .mode column
    pragma table_info('records');
    ```

    The first two commands turn header more on and then format the presentation of data by column. This is what we'll get in return:
    ```sql
    cid         name        type        notnull     dflt_value  pk
    ----------  ----------  ----------  ----------  ----------  ----------
    0           id          TEXT        0                       0
    1           year        TEXT        0                       0
    2           issue_d     TEXT        0                       0
    3           final_d     TEXT        0                       0
    4           emp_length  TEXT        0                       0
    5           home_owner  TEXT        0                       0
    6           home_owner  TEXT        0                       0
    7           income_cat  TEXT        0                       0
    8           annual_inc  TEXT        0                       0
    9           income_cat  TEXT        0                       0
    10          loan_amoun  TEXT        0                       0
    11          term        TEXT        0                       0
    12          term_cat    TEXT        0                       0
    13          applicatio  TEXT        0                       0
    14          applicatio  TEXT        0                       0
    15          purpose     TEXT        0                       0
    16          purpose_ca  TEXT        0                       0
    17          interest_p  TEXT        0                       0
    18          interest_p  TEXT        0                       0
    19          loan_condi  TEXT        0                       0
    20          loan_condi  TEXT        0                       0
    21          interest_r  TEXT        0                       0
    22          grade       TEXT        0                       0
    23          grade_cat   TEXT        0                       0
    24          dti         TEXT        0                       0
    25          total_pymn  TEXT        0                       0
    26          total_rec_  TEXT        0                       0
    27          recoveries  TEXT        0                       0
    28          installmen  TEXT        0                       0
    29          region      TEXT        0                       0
    ```  

7. Since you're in the SQLite shell, you can also perform your queries by writing SQL directly:
    ```sql
    SELECT * FROM records LIMIT 5;
    ```
    
    Remember to end your SQL statement with a semicolon (`;`). Semicolon is the standard way to terminate a SQL statement.

    This queries all the columns from `records` and return the first 5 rows:
    
    ```sql
    1077501,2011,01/12/2011,1012015,10.0RENT,1,Low,24000,1,5000," 36 months",1INDIVIDUAL,1,credit_card,1,Low,1,"GoodLoan",0,10.65,B,2,27.65,5861.071414,50000,0.0,162.87,munster
    1077430,2011,01/12/2011,1042013,0.5,RENT,1,Low,30000,1,2500," 60 months",2,INDIVIDUAL,1,car,2,High,2,"Bad Loan",1,15.27,C,3,1.0,1008.71,456.46,117.08,59.83,leinster
    1077175,2011,01/12/2011,1062014,10.0,RENT,1,Low,12252,1,2400," 36 months",1,INDIVIDUAL,1,small_business,3,High,2,"Good Loan",0,15.96,C,3,8.72,3003.653644,2400.0,0.0,84.33,cannught
    1076863,2011,01/12/2011,1012015,10.0,RENT,1,Low,49200,1,10000," 36 months",1,INDIVIDUAL,1,other,4,High,2,"Good Loan",0,13.49,C,3,20.0,12226.30221,10000.0,0.0,339.31,ulster
    1075358,2011,01/12/2011,1012016,1.0,RENT,1,Low,80000,1,3000," 60 months",2,INDIVIDUAL,1,other,4,Low,1,"Good Loan",0,12.69,B,2,17.94,3242.17,2233.1,0.0,67.79,ulster
    ```

8. Notice that you can write your SQL statements in new lines if you want. The following statement put each clause in its own line:

    ```sql
    sqlite> SELECT sql
   ...> FROM sqlite_master
   ...> WHERE name = 'records';
    ```

    This returns the same output as `.schema records` from step 5 above:

    ```sql
    sql
    -----------------------------------
    CREATE TABLE records(
    "id" TEXT,
    "year" TEXT,
    "issue_d" TEXT,
    "final_d" TEXT,
    "emp_length_int" TEXT,
    "home_ownership" TEXT,
    "home_ownership_cat" TEXT,
    "income_category" TEXT,
    "annual_inc" TEXT,
    "income_cat" TEXT,
    "loan_amount" TEXT,
    "term" TEXT,
    "term_cat" TEXT,
    "application_type" TEXT,
    # truncated
    ...
    )
    ```

9. To exit SQLite dbshell, type `.quit` into your shell and you will now exit the command line interface of sqlite:

    ```sql
    .quit
    ```

If you work in Python and prefer to interact with SQL in a more "python-native" environment, you will likely want to use something known as the ORM. The most popular ORM is SQLAlchemy and I have a 3-part, in-depth guide on SQLAlchemy and working with it in Python. Code samples, datasets, and explanatory guide are all [available free on my GitHub repository](https://github.com/onlyphantom/sqlalchemy-tutorial).