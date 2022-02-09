from unicodedata import decomposition


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0, balance = 0):
        self.intrate = int_rate
        self.account_balance = balance


# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance *= 1.01
        return self

account1 = BankAccount(0, 500)
account2 = BankAccount(0,10000)
account3 = BankAccount(0,10)

account1.deposit(500).deposit(500).deposit(500).withdraw(100).yield_interest().display_account_info()
account3.deposit(500).deposit(500).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


