import base64
import mysql.connector

def retrieve_png_from_mysql(output_path, db_config):
     # Connect to the MySQL database
     connection = mysql.connector.connect(**db_config)
     cursor = connection.cursor()
     # Retrieve the encoded string from the database
     query = "SELECT signed FROM mysign ORDER BY id DESC LIMIT 1"
     cursor.execute(query)
     result = cursor.fetchone()
     if result is None:
          raise ValueError("No data found in the database")
     encoded_string = result[0]
     # Decode the base64 string
     decoded_bytes = base64.b64decode(encoded_string)
     # Write the decoded bytes to a new PNG file
     with open(output_path, 'wb') as file:
          file.write(decoded_bytes)
     # Close the connection
     cursor.close()
     connection.close()

if __name__ == "__main__":
     # Define the path to your PNG file and your database configuration
     png_path = 'sign.png'
     db_config = {
          'user': 'root',
          'password': 'password',
          'host': '127.0.0.1',
          'database': 'poc'
     }
      # Retrieve the PNG file from the MySQL database and save it as signnew.png
     output_path = 'signnew.png'
     retrieve_png_from_mysql(output_path, db_config)
