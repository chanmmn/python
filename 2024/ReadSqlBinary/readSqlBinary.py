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

# Read the binary data from the database
query = f"SELECT {column_name} FROM {table_name} WHERE id = ?"
cursor.execute(query, (1,))  # Assuming you want to read the image with id 1
row = cursor.fetchone()

if row:
    binary_data = row[0]
    # Write the binary data to a new image file
    with open('imagenew.png', 'wb') as file:
        file.write(binary_data)

print("Image file has been read from the database and saved as imagenew.png.")

# Close the connection
cursor.close()
conn.close()