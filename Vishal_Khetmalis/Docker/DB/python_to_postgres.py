import psycopg2

hostname = 'host.docker.internal'
#hostname = 'localhost'
database = 'imdb'
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

    cur.execute('Select * from director_mapping limit 5')
    for records in cur.fetchall():
        print(records)

    cur.execute('Select * from genre limit 5')
    for records in cur.fetchall():
        print(records)

    cur.execute('Select * from movie limit 5')
    for records in cur.fetchall():
        print(records)

    cur.execute('Select * from names limit 5')
    for records in cur.fetchall():
        print(records)

    cur.execute('Select * from ratings limit 5')
    for records in cur.fetchall():
        print(records)

    cur.execute('Select * from role_mapping limit 5')
    for records in cur.fetchall():
        print(records)

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()