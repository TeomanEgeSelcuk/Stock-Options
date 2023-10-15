    # host= os.getenv("DATABASE_HOST"),
    # user=os.getenv("DATABASE_USERNAME"),
    # passwd= os.getenv("DATABASE_PASSWORD"),
    # db= os.getenv("DATABASE")

import mysql.connector
import os 

# MySQL server connection parameters
config = {
    "host": os.getenv("DATABASE_HOST"),
    "user": os.getenv("DATABASE_USERNAME"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "database": os.getenv("DATABASE")
}

# Connect to the MySQL server
try:
    connection = mysql.connector.connect(**config)
    print("Connected to MySQL Server")

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Execute a simple query
    cursor.execute("SELECT * FROM your_table_name")

    # Fetch the results
    results = cursor.fetchall()

    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
