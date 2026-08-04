from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw_data.xlsx"
OUTPUT_FILE = BASE_DIR / "data" / "customers.csv"


# Read the Excel file
df = pd.read_excel(INPUT_FILE)

# Keep only customer names
customers = df[["Customer Name"]].copy()

# Remove duplicate customers
customers = customers.drop_duplicates().reset_index(drop=True)

# Generate Customer IDs
customers.insert(
    0,
    "Customer ID",
    [f"CUST{index:05d}" for index in range(1, len(customers) + 1)]
)

# Generate Email Addresses
customers["Email"] = (
    customers["Customer Name"]
        .str.strip()
        .str.lower()
        .str.replace(" ", ".", regex=False)
        + "@pythonbank.com"
)

# Save the new CSV
customers.to_csv(OUTPUT_FILE, index=False)

print("=" * 50)
print("Customers file created successfully!")
print(f"Location : {OUTPUT_FILE}")
print(f"Total Customers : {len(customers)}")
print("=" * 50)