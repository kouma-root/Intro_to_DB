import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root'
)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except mysql.connector.Error as e:
    print(e)
else:
    print("Database 'alx_book_store' created successfully!")
mycursor.close()
mydb.close()