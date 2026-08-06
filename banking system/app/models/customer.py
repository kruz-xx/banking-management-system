"""
Customer Model

Defines the Customer class, which stores information
about individual bank customers.
"""


class Customer:
    """
    Represents a customer of the bank.
    """

    def __init__(self, customer_id, customer_name):
        """
        Initializes a Customer object.
        """

        self.customer_id = customer_id
        self.customer_name = customer_name

    def display_customer_info(self):
        """
        Displays customer information.
        """

        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")