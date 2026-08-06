class Account:
    def __init__(self, account_id, customer_id, account_type, branch, balance, currency):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.branch = branch
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        
        self.balance += amount
        print(f"Deposited {amount} {self.currency}. New balance: {self.balance} {self.currency}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} {self.currency}. New balance: {self.balance} {self.currency}.")
            
    def display_account_info(self):
        print(f"Account ID: {self.account_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Branch: {self.branch}")
        print(f"Balance: {self.balance} {self.currency}")