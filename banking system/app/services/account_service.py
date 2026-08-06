"""
Account Service

This module contains the business logic for account related operations.
It acts as an intermediary between the data layer (Account model) and the user interface.
"""

class AccountService:
    """ Manages all account operations such as searching, depositing,
    withdrawing, transferring and displaying accounts."""
    
    def __init__(self):
       # Initializes an empty list to store Account objects.
        self.accounts = []
    
    def add_account(self, account):
        # Adds a new account object to the list of accounts.
        self.accounts.append(account)
        
    def display_accounts(self):
        # Displays information for all accounts in the system.
        if not self.accounts:
            print("No accounts available.")
            return
        
        for account in self.accounts:
            account.display_account_info()
            print("-" * 30)
            
    def search_account(self, account_id):
        # Searches for an account by its ID and returns the account object if found.
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None
    
    def deposit(self, account_id, amount):
        # Deposits a specified amount into the account with the given ID after validating the amount.
        account = self.find_account_by_id(account_id)
        
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        
        if account:
            account.balance += amount
            print(f"Deposited {amount} to account {account_id}. New balance: {account.balance}")
        else:
            print(f"Account with ID {account_id} not found.")
            
    def withdraw(self, account_id, amount):
        # Withdraws a specified amount from the account with the given ID after validating the amount and checking for sufficient funds.
        account = self.find_account_by_id(account_id)
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        if account:
            if account.balance >= amount:
                account.balance -= amount
                print(f"Withdrew {amount} from account {account_id}. New balance: {account.balance}")
            else:
                print(f"Insufficient funds in account {account_id}. Current balance: {account.balance}")
        else:
            print(f"Account with ID {account_id} not found.") 
            
    def transfer(self, from_account_id, to_account_id, amount):
        # Transfers money from one account to another
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        
        sender = self.find_account_by_id(from_account_id)
        receiver = self.find_account_by_id(to_account_id)
        
        if sender is None:
            print("sender account not found.")
            return
        
        if receiver is None:
            print("receiver account not found.")
            return
        
        if sender.balance < amount:
            print("Insufficient funds in sender's account.")
            return
        
        # Withdraw from sender and deposit into receiver
        sender.withdraw(amount)
        receiver.deposit(amount)
        
        print(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
        print("Transfer completed successfully.")