import pandas as pd


df = pd.read_csv(
    "D:/Projects/RMG_BI_Automation_Project/data/raw/production_raw.csv"
)


print(df.head())


print("\nTotal Records:")
print(len(df))


print("\nColumns:")
print(df.columns)