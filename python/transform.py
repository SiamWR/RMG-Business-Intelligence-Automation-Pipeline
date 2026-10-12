import pandas as pd
import numpy as np
from datetime import datetime



# =====================================================
# FACTORY DIMENSION TRANSFORMATION
# =====================================================

def clean_factory(df):

    print("Cleaning factory data...")


    # Remove duplicate factories

    df = df.drop_duplicates(
        subset=["Factory_ID"]
    )


    # Standardize text

    df["Factory_Name"] = (
        df["Factory_Name"]
        .str.strip()
        .str.title()
    )


    df["Location"] = (
        df["Location"]
        .str.strip()
        .str.title()
    )


    df["Factory_Type"] = (
        df["Factory_Type"]
        .str.strip()
        .str.title()
    )


    df["Data_Status"] = "Clean"


    return df




# =====================================================
# PRODUCT DIMENSION TRANSFORMATION
# =====================================================

def clean_product(df):

    print("Cleaning product data...")


    df = df.drop_duplicates(
        subset=["Product_ID"]
    )


    df["Product_Name"] = (
        df["Product_Name"]
        .str.strip()
        .str.title()
    )


    df["Category"] = (
        df["Category"]
        .str.strip()
        .str.title()
    )


    df["Buyer"] = (
        df["Buyer"]
        .str.strip()
        .str.title()
    )


    # Invalid cost handling

    df.loc[
        df["Unit_Cost"] < 0,
        "Unit_Cost"
    ] = np.nan


    df["Unit_Cost"] = (
        df["Unit_Cost"]
        .fillna(
            df["Unit_Cost"].median()
        )
    )


    df["Data_Status"] = "Clean"


    return df




# =====================================================
# DATE DIMENSION TRANSFORMATION
# =====================================================

def clean_date(df):

    print("Cleaning date data...")


    df["Date"] = pd.to_datetime(
        df["Date"]
    )


    df = df.drop_duplicates(
        subset=["Date"]
    )


    df = df.sort_values(
        "Date"
    )


    df["Data_Status"] = "Clean"


    return df




# =====================================================
# PRODUCTION VALIDATION
# =====================================================

def validate_production(df):

    print("Validating production data...")


    errors = []


    # Missing critical values

    critical_columns = [
        "Production_ID",
        "Date",
        "Factory_ID",
        "Product_ID",
        "Target_Output",
        "Actual_Output"
    ]


    missing = df[
        df[critical_columns]
        .isnull()
        .any(axis=1)
    ].copy()


    if len(missing) > 0:

        missing["Error_Type"] = (
            "Missing Critical Field"
        )

        errors.append(missing)



    # Negative production

    negative = df[
        df["Actual_Output"] < 0
    ].copy()


    if len(negative) > 0:

        negative["Error_Type"] = (
            "Negative Production"
        )

        errors.append(negative)



    if len(errors) > 0:

        return pd.concat(
            errors,
            ignore_index=True
        )


    return pd.DataFrame()




# =====================================================
# PRODUCTION FACT TRANSFORMATION
# =====================================================

def clean_production(df):

    print("Cleaning production data...")


    # Remove duplicates

    df = df.drop_duplicates(
        subset=["Production_ID"]
    )


    # Remove only critical missing values

    df = df.dropna(
        subset=[
            "Production_ID",
            "Date",
            "Factory_ID",
            "Product_ID",
            "Target_Output",
            "Actual_Output"
        ]
    )


    # Handle optional missing data

    df["Defect_Count"] = (
        df["Defect_Count"]
        .fillna(0)
    )


    df["Workers"] = (
        df["Workers"]
        .fillna(
            df["Workers"].median()
        )
    )


    df["Working_Hours"] = (
        df["Working_Hours"]
        .fillna(
            df["Working_Hours"].median()
        )
    )


    # Date conversion

    df["Date"] = pd.to_datetime(
        df["Date"]
    )


    # KPI calculation

    df["Efficiency"] = np.where(

        df["Target_Output"] > 0,

        (
            df["Actual_Output"]
            /
            df["Target_Output"]
        ) * 100,

        0
    )



    df["Defect_Rate"] = np.where(

        df["Actual_Output"] > 0,

        (
            df["Defect_Count"]
            /
            df["Actual_Output"]
        ) * 100,

        0
    )



    df["Processed_Date"] = datetime.now()


    df["Data_Status"] = "Clean"


    return df