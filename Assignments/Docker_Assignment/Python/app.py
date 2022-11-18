import mysql.connector

connection = mysql.connector.connect(
    user="root", password="aniket1996", host="mysql", port="3306", database="db")

print("Database Connected...")

cursor=connection.cursor()
cursor.execute("select * from students")
students=cursor.fetchall()
connection.close()

print(students)