class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account Balance for {self.account_holder}: {self.balance}")
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            account = Account(account_number, account_holder, initial_balance)
            self.accounts[account_number] = account
            print(f"Account created for {account_holder} with Account Number {account_number}.")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print("Account not found.")
            return None

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account not found.")


# Example usage
bank = Bank("MyBank")

# Create accounts
bank.create_account("123456", "Alice", 500)
bank.create_account("789012", "Bob", 1000)

# Deposit and withdraw operations for Alice
alice_account = bank.get_account("123456")
if alice_account:
    alice_account.deposit(300)
    alice_account.withdraw(200)
    alice_account.check_balance()
    alice_account.display_account_info()

# Delete Bob's account
bank.delete_account("789012")
