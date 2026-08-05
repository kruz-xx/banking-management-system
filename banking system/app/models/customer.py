class Customer:
    def __init__(self, customer_id, customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name
        
    def display_customer_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        
    customers = []
    
    for row in csv_file:
        customer= Customer(
            row["Customer ID"],
            row["Customer Name"]
        )
        customers.append(customer)
            