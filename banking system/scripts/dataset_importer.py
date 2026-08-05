from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "raw_data.xlsx"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(INPUT_FILE)

customers=[]
accounts=[]
transactions=[]

customer_id_map={}

customer_counter=1
transaction_counter=1

for _, row in df.iterrows():

    account_id = row["Account ID"]
    customer_name = row["Customer Name"]
    account_type = row["Account Type"]
    branch = row["Branch"]
    transaction_type = row["Transaction Type"]
    transaction_amount = row["Transaction Amount"]
    balance = row["Account Balance"]
    currency = row["Currency"]

    if customer_name not in customer_id_map:
        customer_id = f"CUST{customer_counter:04d}"

        customer_id_map[customer_name] = customer_id

        customers.append({
            "Customer ID": customer_id,
            "Customer Name": customer_name
        })

        customer_counter += 1
        
    accounts.append({
        "Account ID": account_id,
        "Customer ID": customer_id_map[customer_name],
        "Account Type": account_type,
        "Branch": branch,
        "Balance": balance,
        "Currency": currency
    })
    
    transaction_id = f"TRANS{transaction_counter:06d}"
    
    transactions.append({
        "Transaction ID": transaction_id,
        "Account ID": account_id,
        "Transaction Type": transaction_type,
        "Transaction Amount": transaction_amount
    })
    
    transaction_counter += 1
    
customers_df = pd.DataFrame(customers)
accounts_df = pd.DataFrame(accounts)
transactions_df = pd.DataFrame(transactions)

customers_df.to_csv(OUTPUT_DIR / "customers.csv", index=False)
accounts_df.to_csv(OUTPUT_DIR / "accounts.csv", index=False)
transactions_df.to_csv(OUTPUT_DIR / "transactions.csv", index=False)
    
print(f"Customers: {len(customers)}")
print(f"Accounts: {len(accounts)}")
print(f"Transactions: {len(transactions)}")

print("CSV files generated successfully!")

