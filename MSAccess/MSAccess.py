import pyodbc

# Set up the connection string
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\ams\PatitentDemo.accdb;'
# Establish a connection to the database
conn = pyodbc.connect(conn_str)
# Create a cursor object to execute SQL queries
cursor = conn.cursor()
# Execute a SELECT query to retrieve data from the Patient table
cursor.execute('SELECT * FROM Patient')
# Fetch all rows from the result set
rows = cursor.fetchall()
# Process the rows
for row in rows:
    # Access individual columns by index or column name
    patient_id = row.PatientID
    first_name = row.FirstName
    last_name = row.LastName
    date_of_birth = row.DateOfBirth
    gender = row.Gender
    address = row.Address
    phone_number = row.PhoneNumber
    # Do something with the data...
    print(f'Patient ID: {patient_id}, Name: {first_name} {last_name}, DOB: {date_of_birth}, Gender: {gender}, Address: {address}, Phone: {phone_number}')
# Close the cursor and connection
cursor.close()
conn.close()