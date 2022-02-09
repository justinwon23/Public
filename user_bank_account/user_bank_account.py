class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = .02, balance = 0):
        self.intrate = int_rate
        self.account = balance



    def deposit(self, amount):
        self.account += amount
        return self
    
    def withdraw(self, amount):
        if self.account < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.account -= 5
        else:
            self.account -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.account}")
        return self

    def yield_interest(self):
        if self.account > 0:
            self.account *= 1.01
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(1.02,0)

user1 = User("Justin Won","codingdojo@python.com")

user1.account.deposit(500).withdraw(100).yield_interest().display_account_info()
# print(user1.account)







