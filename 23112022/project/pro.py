import psycopg2

conn= psycopg2.connect(host="host.docker.internal",port=5432,user="postgres",password="Prathm@1387",database='supplier')

cur=conn.cursor()

cur.execute("SELECT * FROM customers")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communications with database
cur.close()
conn.close()

print("server is starting")