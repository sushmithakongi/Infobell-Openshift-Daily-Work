import psycopg2

conn= psycopg2.connect(host="host.docker.internal",port=5432,user="postgres",password="POSTGRES",database='redbus')

cur=conn.cursor()

cur.execute("SELECT * FROM buses")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communications with database
#host.docker.internal
cur.close()
conn.close()