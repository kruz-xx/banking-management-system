from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

excel_file = BASE_DIR / "data" / "raw_data.xlsx"

df = pd.read_excel(excel_file)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())