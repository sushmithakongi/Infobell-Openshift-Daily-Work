import mysql.connector 
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '192.168.48.2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aniket1996'
app.config['PORT'] = '3308'
app.config['MYSQL_DB'] = 'test'


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        fname = details['fname']
        lname = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO record(fname, lname) VALUES (%s, %s)", (fname, lname))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host ='0.0.0.0')