""" Customer Service

Handles operations related to Customer Objects.
"""
class CustomerService:
    
    # Manages all customer-related operations.
    def __init__(self):
        #Initializes an empty customer list.
        self.customers = []
        
    def add_customer(self, customer):
        # Adds a customer object to the list.
        self.customers.append(customer)
        
    def display_customers(self):
        #Displays all customers and their info.
        for customer in self.customers:
            customer.display_customer_info()
            print("-"*30)
            

        