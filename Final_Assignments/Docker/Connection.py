import psycopg2
from flask import Flask


conn = psycopg2.connect(database="Connection",
                        host="host.docker.internal",
                        user="postgres",
                        password="Infobell@#0088")

cursor = conn.cursor()
cursor.execute("select * from employees")
print(cursor.fetchall())




