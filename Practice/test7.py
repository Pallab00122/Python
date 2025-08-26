# Implement a simple BankAccount class with methods for deposit, withdraw, 
# and get_balance. Ensure withdrawals raise an InsufficientFundsError if needed.

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self,account,balance):
        if balance<0:
            raise ValueError("Initial balance cannot be negative")
        self.account=account
        self.balance=balance
        print(f"Acccount number : {self.account} and Initial balance : {self.balance}")
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive.")
        self.balance -=amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
    def get_balance(self):
        return self.balance

print("--- Creating Account ---")
try:
    my_account = BankAccount("12345", 500)
except ValueError as e:
    print(f"Error creating account: {e}")

print("--- Creating Deposit ---")

try:
    my_account.deposit(200)
    my_account.deposit(0)
except ValueError as e:
    print(f"Error depositinmg {e}")

print("\n--- Testing Withdrawal ---")
try:
    my_account.withdraw(150)
    my_account.withdraw(700)
except InsufficientFundsError as e:
    print(f"Error withdrawing: {e}")

print(f"\n Final Balance fro {my_account.account} : {my_account.balance}")