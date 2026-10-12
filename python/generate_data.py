import pandas as pd
import numpy as np
from faker import Faker
import random
import os


# -----------------------------
# Setup
# -----------------------------

fake = Faker()


# Location where files will be saved

OUTPUT_PATH = "D:/Projects/RMG_BI_Automation_Project/data/raw"


# Create folder if not exists

os.makedirs(
    OUTPUT_PATH,
    exist_ok=True
)


# -----------------------------
# 1. Generate Factory Master
# -----------------------------

def create_factory_data():

    factories = []


    locations = [
        "Gazipur",
        "Dhaka",
        "Narayanganj",
        "Chittagong",
        "Mymensingh"
    ]


    for i in range(1, 6):

        factories.append({

            "Factory_ID": f"F{i:03}",

            "Factory_Name":
            fake.company()
            + " Garments",

            "Location":
            random.choice(locations),

            "Factory_Type":
            random.choice(
                [
                    "Knit",
                    "Woven"
                ]
            ),

            "Daily_Capacity":
            random.randint(
                30000,
                80000
            )
        })


    df = pd.DataFrame(factories)


    df.to_csv(
        f"{OUTPUT_PATH}/factory_raw.csv",
        index=False
    )


    print("Factory data created")



# -----------------------------
# 2. Generate Product Master
# -----------------------------

def create_product_data():

    products = []


    product_names = [

        "Polo Shirt",
        "T-Shirt",
        "Jeans",
        "Jacket",
        "Sweater"

    ]


    buyers = [

        "H&M",
        "Zara",
        "Uniqlo",
        "Target",
        "Levis"

    ]


    for i in range(1,21):

        products.append({

            "Product_ID":
            f"P{i:03}",


            "Product_Name":
            random.choice(product_names),


            "Category":
            random.choice(
                [
                    "Knit",
                    "Woven"
                ]
            ),


            "Buyer":
            random.choice(buyers),


            "Unit_Cost":
            random.randint(
                200,
                1500
            )

        })


    df = pd.DataFrame(products)


    df.to_csv(
        f"{OUTPUT_PATH}/product_raw.csv",
        index=False
    )


    print("Product data created")



# -----------------------------
# 3. Generate Production Data
# -----------------------------

def create_production_data():

    records = []


    dates = pd.date_range(

        start="2026-01-01",

        end="2026-12-31",

        freq="D"

    )


    for i in range(1,20001):


        target = random.randint(
            3000,
            7000
        )


        actual = random.randint(
            2500,
            target
        )


        records.append({

            "Production_ID":
            i,


            "Date":
            random.choice(dates),


            "Factory_ID":
            f"F{random.randint(1,5):03}",


            "Line_ID":
            f"L{random.randint(1,20):02}",


            "Product_ID":
            f"P{random.randint(1,20):03}",


            "Workers":
            random.randint(
                20,
                100
            ),


            "Working_Hours":
            random.randint(
                6,
                10
            ),


            "Target_Output":
            target,


            "Actual_Output":
            actual,


            "Defect_Count":
            random.randint(
                5,
                200
            )

        })


    df = pd.DataFrame(records)


    df.to_csv(

        f"{OUTPUT_PATH}/production_raw.csv",

        index=False

    )


    print("Production data created")

# -----------------------------
# 4. Generate Date Dimension
# -----------------------------

def create_date_data():

    dates = pd.date_range(
        start="2026-01-01",
        end="2026-12-31",
        freq="D"
    )


    date_records = []


    for date in dates:

        date_records.append({

            "Date_ID":
            int(date.strftime("%Y%m%d")),


            "Date":
            date,


            "Day":
            date.day,


            "Month":
            date.month,


            "Month_Name":
            date.strftime("%B"),


            "Quarter":
            f"Q{((date.month-1)//3)+1}",


            "Year":
            date.year,


            "Week_Number":
            date.isocalendar().week

        })


    df = pd.DataFrame(date_records)


    df.to_csv(
        f"{OUTPUT_PATH}/date_raw.csv",
        index=False
    )


    print("Date data created")

# -----------------------------
# Main Program
# -----------------------------

if __name__ == "__main__":


    print(
        "Starting RMG Data Generation..."
    )


    create_factory_data()


    create_product_data()


    create_date_data()


    create_production_data()


    print(
        "All raw data generated successfully!"
    )