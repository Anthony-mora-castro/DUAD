class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} units. Current balance: {self.balance}")
        else:
            print("The deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} units. Current balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Cannot withdraw {amount} units. The minimum allowed balance is {self.min_balance}.")
        else:
            super().withdraw(amount)


# Example usage
try:
    # Create a savings account with an initial balance of 1000 and a minimum balance of 500
    savings_account = SavingsAccount(balance=1000, min_balance=500)

    # Deposit money
    savings_account.deposit(300)  # Current balance: 1300

    # Withdraw money (success)
    savings_account.withdraw(200)  # Current balance: 1100

    # Attempt to withdraw more than allowed (error)
    savings_account.withdraw(700)  # This will raise an error
except ValueError as e:
    print(e)
