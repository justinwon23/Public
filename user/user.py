class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)



justin = User("Justin Won", "codingdojo@python.com")
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

# print(guido.name)
guido.make_deposit(100)
guido.make_deposit(50)
monty.make_deposit(500)
guido.make_withdrawal(75)
guido.make_withdrawal(500)
justin.make_deposit(10000000000)
justin.make_deposit(99999999999999999)
justin.make_deposit(9999999999999999999)
justin.make_withdrawal(10)
monty.make_withdrawal(10)
monty.make_withdrawal(10)
justin.display_user_balance()
guido.display_user_balance()
monty.display_user_balance()


