from mysql.connector import Error
from datetime import datetime

import mysql.connector

def insert_actor(actor_id, first_name, last_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Sakila',
            user='root',
            password='password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """INSERT INTO actor (actor_id, first_name, last_name, last_update) 
                              VALUES (%s, %s, %s, %s)"""
            current_time = datetime.now()
            record = (actor_id, first_name, last_name, current_time)
            cursor.execute(insert_query, record)
            connection.commit()
            print("Record inserted successfully into actor table")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage
insert_actor(201, 'John', 'Doe')