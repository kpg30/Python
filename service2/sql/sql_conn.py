import mysql.connector
from mysql.connector import Error

def get_mysql_conn(database: str):
    try:
        if database:   
            conn = mysql.connector.connect(
                host="localhost",  # Replace with your host
                user="root",       # Replace with your MySQL username
                password="Kpg@1993",  # Replace with your MySQL password
                database=database  # Replace with your database name
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",  # Replace with your host
                user="root",       # Replace with your MySQL username
                password="Kpg@1993",  # Replace with your MySQL password
                database="default_db"  # Replace with your database name
            )
        
        if conn.is_connected():
            print("Connected to MySQL.")
            return conn

    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
      
    
