"""
CSV Repository

Responsible for reading processed CSV files
and converting each row into Python objects.

This class separates file handling from the
business logic of the application.
"""

import pandas as pd
from pathlib import Path

from models.customer import Customer
from models.account import Account
from models.transaction import Transaction


class CSVRepository:
    def __init__(self):
        """
Initializes the repository and sets the path
to the processed CSV files.
"""
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.data_dir = self.base_dir / "data" / "processed"
        
        """
Loads customer data from customers.csv
and converts every row into a Customer object.

Returns:
    list[Customer]
"""

    def load_customers(self):
        #READ CSV FILE INTO A PANDAS DATAFRAME
        file = self.data_dir / "customers.csv"

        df = pd.read_csv(file)

        customers = []
        
        #CONVERT EACH ROW INTO A CUSTOMER OBJECT
        for _, row in df.iterrows():
            customer = Customer(
                row["Customer ID"],
                row["Customer Name"]
            )

            customers.append(customer)

        return customers
    
    """
Loads account data from accounts.csv
and converts every row into an Account object.

Returns:
    list[Account]
"""


    def load_accounts(self):
        #READ CSV FILE INTO A PANDAS DATAFRAME
        file = self.data_dir / "accounts.csv"

        df = pd.read_csv(file)

        accounts = []
        
        #CONVERT EACH ROW INTO AN ACCOUNT OBJECT
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
    
    """
Loads transaction data from transactions.csv
and converts every row into a Transaction object.

Returns:
    list[Transaction]
"""

    def load_transactions(self):
        #READ CSV FILE INTO A PANDAS DATAFRAME
        file = self.data_dir / "transactions.csv"

        df = pd.read_csv(file)

        transactions = []
        
        #CONVERT EACH ROW INTO A TRANSACTION OBJECT
        for _, row in df.iterrows():
            transaction = Transaction(
                row["Transaction ID"],
                row["Account ID"],
                row["Transaction Type"],
                row["Transaction Amount"]
            )

            transactions.append(transaction)

        return transactions