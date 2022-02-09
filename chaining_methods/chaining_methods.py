import re


class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self



justin = User("Justin Won", "codingdojo@python.com")
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

# print(guido.name)
guido.make_deposit(100).make_deposit(50).make_deposit(50).make_withdrawal(75).make_withdrawal(75).display_user_balance()

monty.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(75).display_user_balance()


justin.make_deposit(100000).make_deposit(500).make_deposit(500).make_withdrawal(10).display_user_balance()





