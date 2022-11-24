import psycopg2

conn= psycopg2.connect(host="host.docker.internal",port=5432,user="postgres",password="POSTGRES",database='postgres')

cur=conn.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communications with database
#host.docker.internal
cur.close()
conn.close()
