import pymssql
# Database connection parameters
server = 'WIN-86UEG9VIS67'
user = 'sa'
password = 'password'
database = 'Northwind'
# Establish a connection to the database
conn = pymssql.connect(server, user, password, database)
# Create a cursor object
cursor = conn.cursor()
# Execute a query to read data from the products table
cursor.execute('SELECT * FROM products')
# Fetch all rows from the executed query
rows = cursor.fetchall()
# Print the fetched rows
for row in rows:
    print(row)
# Close the cursor and connection
cursor.close()
conn.close()
