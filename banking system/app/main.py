from database.csv_repo import CSVRepository

from services.customer_service import CustomerService
from services.account_service import AccountService
from services.transaction_service import TransactionService

from ui.menu import display_menu

repo = CSVRepository()

customer_service = CustomerService()
account_service = AccountService()
transaction_service = TransactionService()

for customer in repo.load_customers():
    customer_service.add_customer(customer)

for account in repo.load_accounts():
    account_service.add_account(account)

for transaction in repo.load_transactions():
    transaction_service.add_transaction(transaction)

while True:

    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_service.display_customers()

    elif choice == "2":
        account_service.display_accounts()

    elif choice == "3":
        account_id = input("Enter Account ID: ")

        account = account_service.search_account(account_id)

        if account:
            account.display_account_info()
        else:
            print("Account not found.")

    elif choice == "4":
        account_id = input("Enter Account ID: ")
        
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        account_service.deposit(account_id, amount)

    elif choice == "5":
        account_id = input("Enter Account ID: ")
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        account_service.withdraw(account_id, amount)

    elif choice == "6":
        sender = input("Enter Sender Account ID: ")
        receiver = input("Enter Receiver Account ID: ")
        amount = float(input("Enter amount to transfer: "))

        account_service.transfer(sender, receiver, amount)

    elif choice == "7":
        transaction_service.display_transactions()

    elif choice == "8":
        print("Thank you for using BMS!")
        break

    else:
        print("Invalid choice.")