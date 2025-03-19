class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  

    def _deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You made a deposit of {amount}, your new balance is {self.balance}')
        else:
            print(f'The amount has to be more than 0')

    def _withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'You made a withdraw of {amount}, your new balance is {self.balance}')
        else:
            print(f'Insufficient funds or invalid amount')


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance=100):
        self.balance = balance
        self.min_balance = min_balance

    def _withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f'You cannot withdraw that amount because of the minimum allowed balance')
        else:
            BankAccount._withdraw(self, amount)


my_account = BankAccount(balance=0)

my_account._deposit(100) 

my_account._withdraw(50)  

savings_account = SavingsAccount(balance=200, min_balance=100)


try:
    savings_account._withdraw(25)  
except ValueError as e:
    print(e)