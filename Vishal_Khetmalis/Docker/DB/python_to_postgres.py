import psycopg2

hostname = 'host.docker.internal'
database = 'restaurants'
username = 'postgres'
pwd = 'postgress'
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    cur = conn.cursor()

    cur.execute('Select * from price_list')
    print(cur.fetchall())
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()