import pandas as pd
from pathlib import Path

from models.customer import Customer
from models.account import Account
from models.transaction import Transaction


class CSVRepository:
    def __init__(self):
        # Project root (banking system/)
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.data_dir = self.base_dir / "data" / "processed"

    def load_customers(self):
        file = self.data_dir / "customers.csv"

        df = pd.read_csv(file)

        customers = []

        for _, row in df.iterrows():
            customer = Customer(
                row["Customer ID"],
                row["Customer Name"]
            )

            customers.append(customer)

        return customers

    def load_accounts(self):
        file = self.data_dir / "accounts.csv"

        df = pd.read_csv(file)

        accounts = []

        for _, row in df.iterrows():
            account = Account(
                row["Account ID"],
                row["Customer ID"],
                row["Account Type"],
                row["Branch"],
                row["Balance"],
                row["Currency"]
            )

            accounts.append(account)

        return accounts

    def load_transactions(self):
        file = self.data_dir / "transactions.csv"

        df = pd.read_csv(file)

        transactions = []

        for _, row in df.iterrows():
            transaction = Transaction(
                row["Transaction ID"],
                row["Account ID"],
                row["Transaction Type"],
                row["Transaction Amount"]
            )

            transactions.append(transaction)

        return transactions