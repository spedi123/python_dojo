class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balace = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.deposit += amount
        # your code here

    def withdraw(self, amount):
        self.withdraw -= amount
        # your code here

    def display_account_info(self):
        print(f'balance: {self.balance}')

    def yield_interest(self):
        if self.balace > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
            return self


balance_a = BankAccount(0.01, 1000)
balance_b = BankAccount(0.01, 2000)
balance_c = BankAccount(0.01, 3000)

balance_a.disply_account_info()
