from models.transaction import Transaction

transaction = Transaction(
    "TXN000001",
    "ACC0001",
    "Deposit",
    1000
)

transaction.display_transaction_info()