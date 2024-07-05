import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user="root",
    passwd='lucas123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE expense")

print("all Done!1")