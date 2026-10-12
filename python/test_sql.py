from sqlalchemy import create_engine

from config import DATABASE_CONFIG



# Create SQL Server connection string

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



# Create engine

engine = create_engine(
    connection_string
)



try:

    connection = engine.connect()


    print(
        "SQL Server Connection Successful"
    )


    connection.close()


except Exception as error:


    print(
        "Connection Failed"
    )


    print(error)