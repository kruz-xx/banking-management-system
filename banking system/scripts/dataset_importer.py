from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "raw-data.xlsx"
OUTPUT_DIR = BASE_DIR / "data" / "processed-data"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(INPUT_FILE)

customers=[]
accounts=[]
transactions=[]

customer_id_map={}

customer_counter=1
transaction_counter=1

for _, row in df.iterrows():
    account_id = row['Account ID']
    customer_name = row['Customer Name']
    account_type = row['Account Type']
    branch = row['Branch']
    transaction_type = row['Transaction Type']
    transaction_amount = row['Transaction Amount']
    balance = row['Balance']
    currency = row['Currency']
    
    


