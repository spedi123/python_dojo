class BankAccount:
    bank = 'bank of dojo'
    all_accounts = []

    def __init__(self, balance=0, int_rate=0.01,):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            self.balance -= amount
        else:
            self.balance -= amount
        return self

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


class User:
    bank = 'bank of dojo'

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {}

    def display_info(self, account_name):
        print(f'name: {self.name}')
        print(f'email: {self.email}')
        print(f'{account_name} balance: {self.account[account_name].balance}')
        return self

    def deposit(self, account_name, amount):
        self.account[account_name].balance += amount
        return self

    def withdraw(self, account_name, amount):
        self.account[account_name].balance -= amount
        return self

    def add_account(self, account_name, balance=0, int_rate=0.01):
        self.account[account_name] = BankAccount(balance, int_rate)


user1 = User('peter', 'peter@gamil.com')
user1.add_account('checking')
user1.add_account('saving')
user1.deposit('checking', 1500).deposit('saving', 250).withdraw(
    'checking', 1000).display_info('saving').display_info('checking')

# user2 = User('esther', 'esther@gamil.com')
# user2.deposit(3000).deposit(50).withdraw(2000).display_info()
