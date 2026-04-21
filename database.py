import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
        )
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print(f"Connection with database failed: {e}")
        return None

