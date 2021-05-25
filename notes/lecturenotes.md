# Week 1 Notes

### Data Types
1. Our variables can point to a value that may be an integer, float, string, or boolean (`True`, `False`)
    - `x = 3` (int)
    - `x = 3.1` (float)
    - `x = 'Sam'` (str)
    - `x = False` (boolean)

2. Arithmetics work as you expected:
    ```py
    x = 2
    x += 2 
    # the same as: x = x + 2
    x *= 2
    x ** 2
    # returns: 64
    (x + 3) ** (1 - x + (3 // 2))
    ```

3. Use operators like `==`, `<=`, `>=`, `!=` to check for Equality. Python returns True or False (boolean)

4. Collection of items using compound types like List, Tuple and Dictionaries

    ```py
    ls = [0, 2, 4]
    tp = (1, 3, 5)
    dictA = {
        "name": "NTUC Income's Sales Division",
        "bank": "Development Bank of Singapore (DBS)",
        "branch": "Toa Payoh Branch",
        "account": "060-8981188",
        "type": "POSB Savings",
        "debit_cards": 2,
        "account_created": "2007-01-14",
        "balance": 400,
        "main_currency": "SGD",
        "corporate": True
    }
    ```
    4.1 List is mutable; Tuple is immutable
    4.2 To slice a value out from your list, or tuple, use the zero-based indexing. To slice a key-value pair from your dictionary, you would use the name-based indexing
    ```py
    ls[1]
    dictA["account_created"] # returns: 2007-01-14
    ```
    4.3 To add a value to a list, you would use `.append`. For example `ls.append(-15)`. To add a value to a dictionary, you would just assign a key value pair:
    ```py
    dictA["SWIFT"] = 7171
    ```

5. The `if...else` block. Python uses white space as indentation (other languages may use `if(){...}`)
    ```py
    if transaction_card == 'visa':
        apply_charges += 0.1
        if transaction_amount < 50:
            apply_charges += 0.01
            print("Extra surcharge for small amount transactions")
    else:
        print("Accepts Visa only")
    ```

6. Python has facilities to help us create "Control Flows" just like any other programming language. Apart from `if...else`, we also took a look at the `for...in` loop. This works on an iterable (e.g. List, Dictionary, Tuples, Set)

    ```py
    for t in transactions:
        if t['amount'] > 500:
            print("Transaction Amount exceeds daily limit")
        # else if amount is > 300
        elif t['amount'] > 300 and t['twofactorenabled'] == True:
            twofactor(t)
        else:
            t['status'] = 'Success; Transaction has been processed'
    ```

    When using `for...in` to loop through a Dictionary, this will loop through the dictionary keys.

7. List Comprehension allows you to specify your control flow while creating a list:

    ```py
    # non-performing loans
    npl = [ln['case_number'] for ln in loans if ln['overdue_status'] or ln['due'] > 0]
    ```

### SQL Primer

```sql
SELECT 
    transaction_num, 
    SUM(amount) AS Total,
    COUNT(amount) As NumTransactions,
    AVG(CAST(gst AS decimal)) AS AvgGST
FROM creditcards
WHERE 
    amount > 50 OR
    geo NOT IN ('Singapore', 'Indonesia') AND
    terminal LIKE 'home%'
GROUP BY transaction_num
ORDER BY Total
LIMIT 10 OFFSET 1
```