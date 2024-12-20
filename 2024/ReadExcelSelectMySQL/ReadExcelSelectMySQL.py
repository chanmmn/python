
import pandas as pd

import mysql.connector

# Read the Excel file
df = pd.read_excel('POOCheckNameExist.xlsx', usecols=[0])

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='database'
)
cursor = conn.cursor()

# Prepare the query
# query = "SELECT `name` FROM outlets WHERE `name` LIKE  '% %s %'"

# List to store unmatched values
unmatched_values = []

# Check each value in the DataFrame
for value in df['UniqueName']:
    print (value)
    query = "SELECT `name` FROM outlets WHERE `name` LIKE  '%" + value + "%'"
    print (query)
    data = (value,)
    cursor = conn.cursor(buffered=True)
    cursor.execute(query)
    result = cursor.fetchone()
    if result is None:
        unmatched_values.append(value)

# Close the cursor and connection
cursor.close()
conn.close()

# Output unmatched values to a new Excel file
unmatched_df = pd.DataFrame(unmatched_values, columns=['Unmatched Names'])
unmatched_df.to_excel('POONoMatch.xlsx', index=False)
