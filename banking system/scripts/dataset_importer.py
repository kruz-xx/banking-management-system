from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw_data.xlsx"

df = pd.read_excel(INPUT_FILE)

print(f"Loaded {len(df)} records.")

print("\nAccount Types:")
print(df["Account Type"].unique())

print("\nTransaction Types:")
print(df["Transaction Type"].unique())

print("\nCurrencies:")
print(df["Currency"].unique())

print("\nBranches:")
print(df["Branch"].unique())