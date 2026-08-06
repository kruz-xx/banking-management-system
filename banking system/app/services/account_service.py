class AccountService:
    def __init__(self):
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
        
    def display_accounts(self):
        for account in self.accounts:
            account.display_account_info()
            print("-"*30)
            
    def search_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None
    
    def find_account_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None
    
    def deposit(self, account_id, amount):
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
        
        sender.withdraw(amount)
        receiver.deposit(amount)
        
        print(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
        print("Transfer completed successfully.")