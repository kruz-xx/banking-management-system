class Account:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.__pin = pin
        self.balance = balance
        self.transaction_history = []
        
    def deposit(self, amount):
        if amount <=0:
            print("Deposit amount must be positive.")
            return
        
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        if amount > self.balance:
            print("Insufficient funds.")
            return
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")
        
        print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def show_balance(self):
        print(f"Current balance: {self.balance}")
    
    def verify_pin(self, pin):
        return self.__pin == pin
    
    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid PIN.")
    
    def show_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
            return
        
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
    
    def add_transaction(self, transaction):
        pass
    