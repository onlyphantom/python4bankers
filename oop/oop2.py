from datetime import datetime

class Account:
    total_accounts = 0
    interest_rate = 0.04

    def __init__(self, act_no, act_balance, type) -> None:
        self.act_no = act_no
        self.act_balance = act_balance
        self.type = type
        self.created_date = datetime.now()
        Account.total_accounts += 1

    def returns(self, year):
        if self.type == "multiplier":
            return f'You earned an extra 1% and your balance will grow to ${round(self.act_balance * (1 + self.interest_rate + 0.01) ** year, 2)} in {year} year(s).'
        return f'Your balance is worth ${round(self.act_balance * (1 + self.interest_rate) ** year, 2)} in {year} year(s).'

class MultiCurrencyAccount(Account):
    interest_rate = 0.01

    def __init__(self, act_no, act_balance, type) -> None:
        super().__init__(act_no=act_no, act_balance=act_balance, type=type)


print(Account.total_accounts)
accountA = Account(100101011, 100, "savings")
print(accountA.returns(2))
print(Account.total_accounts)
print(accountA.interest_rate)
accountB = Account(100101012, 700, "multiplier")
print(accountB.returns(2))
print(Account.total_accounts)
print(accountA.interest_rate)
# accountC = MultiCurrencyAccount(555101011, 1000, "multi")
# print(Account.total_accounts)
# print(accountC.created_date)
# print(accountC.interest_rate)