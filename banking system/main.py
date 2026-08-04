from account import Account


def main():
    account1 = Account("123456", "John Doe", "1234", 1000)
    
    account1.deposit(500)
    account1.withdraw(200)      
    account1.deposit(-100)  # Invalid deposit
    account1.withdraw(2000)  # Insufficient funds
    account1.show_balance()
    account1.change_pin("1234", "5678")  # Change PIN successfully
    account1.change_pin("0000", "5678")  # Invalid PIN
    account1.show_history()

if __name__ == "__main__":
    main()