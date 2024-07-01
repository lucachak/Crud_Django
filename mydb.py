import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user="****",
    passwd='*******'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE myDB")

print("all Done!1")