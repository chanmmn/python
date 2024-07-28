import psycopg2
# Define the database connection parameters
db_params = {
	"host": "your_host",	 # Replace with your PostgreSQL host
	"database": "test",
	"user": "your_username", # Replace with your PostgreSQL username
	"password": "your_password"  # Replace with your PostgreSQL password
}
try:
	# Connect to the PostgreSQL database
	connection = psycopg2.connect(**db_params)
	# Create a cursor object
	cursor = connection.cursor()
	# Define your SQL query to select data from the "person" table
	select_query = "SELECT * FROM person"
	# Execute the SQL query
	cursor.execute(select_query)
	# Fetch all rows from the result set
	rows = cursor.fetchall()
	# Display the data
	for row in rows:
		print(row)
except psycopg2.Error as e:
	print("Error connecting to the PostgreSQL database:", e)
finally:
	if connection:
		# Close the cursor and connection
		cursor.close()
		connection.close()
