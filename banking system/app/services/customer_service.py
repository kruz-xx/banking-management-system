class CustomerService:
    def __init__(self):
        self.customers = []
        
    def add_customer(self, customer):
        self.customers.append(customer)
        
    def display_customers(self):
        for customer in self.customers:
            customer.display_customer_info()
            print("-"*30)
            

        