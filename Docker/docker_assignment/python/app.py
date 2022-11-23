import mysql.connector

connection = mysql.connector.connect(
    user="root", password="Psai@777", host="mysql", port="3306", database="dockerdemo")

print("Database Connected...")

cursor = connection.cursor()
cursor.execute("select * from students")
students = cursor.fetchall()
connection.close()

print(students)
