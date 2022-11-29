from flask import Flask
import psycopg2

app = Flask(__name__)

conn= psycopg2.connect(host="host.docker.internal",port=5432,user="postgres",password="Prathm@1387",database='supplier')

cur=conn.cursor()

cur.execute("SELECT * FROM customers")
rows = cur.fetchall()
#for row in rows:
 #   print(row)

# Close communications with database
cur.close()
conn.close()


@app.route('/')
@app.route('/home')
def home():
    return rows




if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)