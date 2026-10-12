import pandas as pd


RAW_PATH = "D:/Projects/RMG_BI_Automation_Project/data/raw"



def extract_factory():

    df = pd.read_csv(
        f"{RAW_PATH}/factory_raw.csv"
    )

    print("Factory data extracted")

    return df



def extract_product():

    df = pd.read_csv(
        f"{RAW_PATH}/product_raw.csv"
    )

    print("Product data extracted")

    return df



def extract_date():

    df = pd.read_csv(
        f"{RAW_PATH}/date_raw.csv"
    )

    print("Date data extracted")

    return df



def extract_production():

    df = pd.read_csv(
        f"{RAW_PATH}/production_raw.csv"
    )

    print("Production data extracted")

    return df