import mysql.connector
dataBase = mysql.connector.Connect(
    host='localhost',
    user='root',
    passwd='root',
)


cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print('All done')
