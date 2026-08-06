"""
Transaction Model

Represents banking transactions such as deposits,
withdrawals, and transfers.
"""


class Transaction:
    """
    Represents a transaction performed on an account.
    """

    def __init__(self, transaction_id, account_id, transaction_type, amount):
        """
        Initializes a Transaction object.
        """

        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount

    def display_transaction_info(self):
        """
        Displays transaction details.
        """

        print(f"Transaction ID: {self.transaction_id}")
        print(f"Account ID: {self.account_id}")
        print(f"Transaction Type: {self.transaction_type}")
        print(f"Amount: {self.amount}")