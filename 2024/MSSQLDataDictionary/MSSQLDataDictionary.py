
import pandas as pd
import pyodbc

def generate_data_dictionary(server, database, username, password):
# Establish a connection to the MS SQL database
connection_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
connection = pyodbc.connect(connection_string)

# Retrieve table names
cursor = connection.cursor()
table_names_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
cursor.execute(table_names_query)
table_names = [row.TABLE_NAME for row in cursor.fetchall()]


# Create a list to store table information
data_dictionary = []

# Retrieve column information for each table
for table_name in table_names:
    column_info_query = f"SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
    cursor.execute(column_info_query)
    columns = cursor.fetchall()

    # Store column information in a list of dictionaries
    for column in columns:
        column_info = {
            'Table': table_name,
            'Column': column.COLUMN_NAME,
            'Data Type': column.DATA_TYPE,
            'Max Length': column.CHARACTER_MAXIMUM_LENGTH,
            'Nullable': column.IS_NULLABLE
        }
        data_dictionary.append(column_info)

# Close the cursor and connection
cursor.close()
connection.close()

return data_dictionary

# Provide the connection details
server = 'Wlocalhost'
database = 'database'
username = 'sa'
password = 'password'

# Generate the data dictionary
data_dict = generate_data_dictionary(server, database, username, password)

# Create a pandas DataFrame from the data dictionary
data_dict_df = pd.DataFrame(data_dict)

# Write the DataFrame to an Excel file
excel_file_path = 'data_dictionary.xlsx'
data_dict_df.to_excel(excel_file_path, index=False)
print(f"Data dictionary has been saved to {excel_file_path}.")