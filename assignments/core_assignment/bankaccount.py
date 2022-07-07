class BankAccount:
    bank = 'bank of dojo'
    all_accounts = []

    def __init__(self, balance=0, int_rate=0.01,):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    print(all_accounts)
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            self.balance -= amount
        else:
            self.balance -= amount
        return self

        # your code here

    def display_account_info(self):
        print(f'bank: {self.bank}')
        print(f'balance: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        else:
            self.balance
        return self

    @classmethod
    def bank_account_info(cls, bank_name):
        cls.bank = bank_name

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum


user_a = BankAccount(1000)
user_b = BankAccount(2000)
user_c = BankAccount(3000)

user_a.deposit(1000).deposit(3000).deposit(2000).withdraw(
    500).yield_interest().display_account_info()
user_b.deposit(500).deposit(2000).withdraw(2200).withdraw(
    520).withdraw(1500).yield_interest().display_account_info()
user_c.deposit(100).withdraw(3500).yield_interest(
).display_account_info()
