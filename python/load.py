from sqlalchemy import create_engine
import os


from config import DATABASE_CONFIG



# =====================================================
# ERROR PATH CONFIGURATION
# =====================================================

ERROR_PATH = (
    "D:/Projects/RMG_BI_Automation_Project/data/errors"
)


os.makedirs(
    ERROR_PATH,
    exist_ok=True
)



# =====================================================
# CREATE SQL SERVER CONNECTION
# =====================================================


def create_connection():


    connection_string = (

        "mssql+pyodbc://@"

        + DATABASE_CONFIG["server"]

        + "/"

        + DATABASE_CONFIG["database"]

        + "?driver="

        + DATABASE_CONFIG["driver"].replace(
            " ",
            "+"
        )

    )


    engine = create_engine(
        connection_string
    )


    return engine



# =====================================================
# GENERIC DATABASE LOADER
# =====================================================


def load_to_database(df, table_name):


    engine = create_connection()


    print(
        f"Loading {table_name}..."
    )


    df.to_sql(

        name=table_name,

        con=engine,

        if_exists="replace",

        index=False

    )


    print(
        f"{table_name} loaded successfully"
    )



# =====================================================
# LOAD DIMENSION TABLES
# =====================================================


def load_factory(df):

    load_to_database(

        df,

        "dim_factory"

    )



def load_product(df):

    load_to_database(

        df,

        "dim_product"

    )



def load_date(df):

    load_to_database(

        df,

        "dim_date"

    )



# =====================================================
# LOAD FACT TABLE
# =====================================================


def load_production(df):

    load_to_database(

        df,

        "fact_production"

    )



# =====================================================
# SAVE ERROR RECORDS
# =====================================================


def load_errors(df):


    if df.empty:


        print(
            "No error records found"
        )

        return



    print(
        "Saving error records..."
    )


    file_path = (

        f"{ERROR_PATH}/production_errors.csv"

    )


    df.to_csv(

        file_path,

        index=False

    )


    print(
        "Error file saved"
    )