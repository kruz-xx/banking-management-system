from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
excel_file = BASE_DIR / "data" / "raw_data.xlsx"

df = pd.read_excel(excel_file)

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nACCOUNT TYPES")
print(df["Account Type"].value_counts())

print("\nTRANSACTION TYPES")
print(df["Transaction Type"].value_counts())

print("\nBRANCHES")
print(df["Branch"].value_counts())

print("\nCURRENCIES")
print(df["Currency"].value_counts())

print("\nUnique Customers:", df["Customer Name"].nunique())
print("Unique Accounts:", df["Account ID"].nunique())

