
import mysql.connector

try:
        
    alx_book_store_connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "senyo"
    )

    if alx_book_store_connection.is_connected():

        new_cursor = alx_book_store_connection.cursor()
        new_cursor.execute("CREATE DATABASE alx_book_store")

        print("Database 'alx_book_store' created successfully!")
        
except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally: 
    if "alx_book_store_connection" in locals() and alx_book_store_connection.is_connected():
        new_cursor.close()
        alx_book_store_connection.close()

