import base64
import mysql.connector

def store_png_to_mysql(png_path, db_config):
     # Read the PNG file and encode it in base64
     with open(png_path, 'rb') as file:
          encoded_string = base64.b64encode(file.read()).decode('utf-8')
     # Ensure the encoded string fits in the VARCHAR(191) column
     if len(encoded_string) > 1000:
          raise ValueError("Encoded string is too long to fit in VARCHAR(191)")
     # Connect to the MySQL database
     connection = mysql.connector.connect(**db_config)
     cursor = connection.cursor()
     # Insert the encoded string into the database
     query = "INSERT INTO mysign (id, signed) VALUES (1, %s)"
     cursor.execute(query, (encoded_string,))
     connection.commit()
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
     # Store the PNG file in the MySQL database
     store_png_to_mysql(png_path, db_config)



