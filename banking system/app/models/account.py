"""
Account Model

This module defines the Account class, which represents a bank account
in the Banking Management System. It stores account information and
provides methods to perform banking operations such as deposit,
withdrawal, and displaying account details.
"""


class Account:
    """
    Represents a customer's bank account.

    Attributes:
        account_id (str): Unique account identifier.
        customer_id (str): ID of the account holder.
        account_type (str): Type of account (Savings, Current, etc.).
        branch (str): Branch where the account was opened.
        balance (float): Current account balance.
        currency (str): Currency used by the account.
    """

    def __init__(self, account_id, customer_id, account_type, branch, balance, currency):
        """
        Initializes an Account object with its details.
        """

        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.branch = branch
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        """
        Deposits money into the account after validating the amount.
        """

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"Deposited {amount} {self.currency}.")
        print(f"New Balance: {self.balance} {self.currency}")

    def withdraw(self, amount):
        """
        Withdraws money from the account if sufficient funds are available.
        """

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount
        print(f"Withdrew {amount} {self.currency}.")
        print(f"New Balance: {self.balance} {self.currency}")

    def display_account_info(self):
        """
        Displays all account details.
        """

        print(f"Account ID: {self.account_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Branch: {self.branch}")
        print(f"Balance: {self.balance} {self.currency}")