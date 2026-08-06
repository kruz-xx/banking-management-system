"""Transaction Service

Handles all operations related to banking transactions
"""

class TransactionService:
    # Manages all transaction objects
    
    def __init__(self):
        #Initializes an empty transaction list.
        self.transactions = []

    def add_transaction(self, transaction):
        #Adds a transaction to the list.
        self.transactions.append(transaction)

    def display_transactions(self):
        #Displays all recorded transactions.
        for transaction in self.transactions:
            transaction.display_transaction_info()
            print("-" * 30)