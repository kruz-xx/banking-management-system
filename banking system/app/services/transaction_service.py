class TransactionService:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_transactions(self):
        for transaction in self.transactions:
            transaction.display_transaction_info()
            print("-" * 30)