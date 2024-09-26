import pyodbc

# Database connection parameters
server = 'localhost'
database = 'poc'
username = 'sa'
password = 'Pa$$w0rd'
table_name = 'mysign'
column_name = 'signed'
image_path = 'image.png'

# Establish a database connection
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

# Read the image file
with open(image_path, 'rb') as file:
    binary_data = file.read()

# Insert the binary data into the database
query = f"INSERT INTO {table_name} ({column_name}) VALUES (?)"
cursor.execute(query, (pyodbc.Binary(binary_data),))
conn.commit()

print("Image file has been written to the database.")

# Close the connection
cursor.close()
conn.close()