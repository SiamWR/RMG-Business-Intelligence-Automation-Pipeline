import pandas as pd


df = pd.read_csv(
    "D:/Projects/RMG_BI_Automation_Project/data/raw/date_raw.csv"
)


print(df.head())

print("\nRows:")
print(len(df))