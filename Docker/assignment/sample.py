from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(host="host.docker.internal", port=5432,
                        user="postgres", password="sai@123", database='students')

cur = conn.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()
# for row in rows:
#   print(row)

# Close communications with database
cur.close()
conn.close()
print(rows)


@app.route('/')
@app.route('/home')
def home():
    return rows


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='localhost', port=5000)
