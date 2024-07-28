import pandas as pd
import mysql.connector

# Define MySQL database connection parameters
db_config = {
    'host': 'localhost',       # Change to your MySQL host
    'user': 'your_username',   # Change to your MySQL username
    'password': 'your_password',  # Change to your MySQL password
    'database': 'database'
}

# Read the Excel file into a DataFrame
excel_file = 'StateToClean.xlsx'
df = pd.read_excel(excel_file)

# Establish a connection to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Loop through the DataFrame and update the MySQL table
    for index, row in df.iterrows():
        id_value = row['id']
        state = row['state']

        # Update the MySQL table
        sql = "UPDATE outlets SET state = %s WHERE id = %s"
        cursor.execute(sql, (state, id_value))
        conn.commit()

    print("Database updated successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and database connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
