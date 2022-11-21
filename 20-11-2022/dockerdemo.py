import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="malkeet",
    user="postgres",
    password="postgres",
    host="127.0.0.1"
)

# Open cursor to perform database operation
cur = conn.cursor()

# Query the database 
cur.execute("SELECT * FROM demo1")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communications with database
cur.close()
conn.close()