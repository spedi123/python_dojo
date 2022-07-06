class Account:
    def __init__(self, name, initial_amount):
        self.name = name
        self.balance = initial_amount

    def display_user_balance(self):
        print(f'name: {self.name} ; balance: {self.balance}')

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self


user_a = Account("peter", 1000)
user_b = Account("esther", 2000)
user_c = Account("riley", 3000)
user_d = Account("brian", 4000)

user_a.deposit(50).withdraw(1000).display_user_balance()
user_b.deposit(300).withdraw(3000).display_user_balance()
user_c.deposit(3000).withdraw(2000).display_user_balance()
