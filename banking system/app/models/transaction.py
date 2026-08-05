class Transaction:
    def __init__(self, transaction_id, account_id, transaaction_type, amount):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaaction_type = transaaction_type
        self.amount = amount
        
    def display_transaction_info(self):
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Account ID: {self.account_id}")
        print(f"Transaction Type: {self.transaaction_type}")
        print(f"Amount: {self.amount}")