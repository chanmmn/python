import pyodbc
import pandas as pd

# Connect to the SQL Server database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=northwind;Trusted_Connection=yes;TrustServerCertificate=true')

# Retrieve primary keys information
primary_keys_query = """
SELECT
    TABLE_NAME,
    COLUMN_NAME
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    CONSTRAINT_NAME LIKE 'PK_%'
"""
primary_keys_df = pd.read_sql_query(primary_keys_query, conn)

# Retrieve foreign keys information
foreign_keys_query = """
SELECT
    FK.TABLE_NAME AS 'Table Name',
    CU.COLUMN_NAME AS 'Column Name',
    PK.TABLE_NAME AS 'Referenced Table',
    PT.COLUMN_NAME AS 'Referenced Column'
FROM
    INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS AS C
    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS FK ON C.CONSTRAINT_NAME = FK.CONSTRAINT_NAME
    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS PK ON C.UNIQUE_CONSTRAINT_NAME = PK.CONSTRAINT_NAME
    INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS CU ON C.CONSTRAINT_NAME = CU.CONSTRAINT_NAME
    INNER JOIN (
        SELECT
            i1.TABLE_NAME,
            i2.COLUMN_NAME
        FROM
            INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS i1
            INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS i2 ON i1.CONSTRAINT_NAME = i2.CONSTRAINT_NAME
        WHERE
            i1.CONSTRAINT_TYPE = 'PRIMARY KEY'
    ) AS PT ON PT.TABLE_NAME = PK.TABLE_NAME
"""
foreign_keys_df = pd.read_sql_query(foreign_keys_query, conn)

# Export the data to an Excel file
with pd.ExcelWriter('outsystems_qa_keys.xlsx') as writer:
    primary_keys_df.to_excel(writer, sheet_name='Primary Keys', index=False)
    foreign_keys_df.to_excel(writer, sheet_name='Foreign Keys', index=False)