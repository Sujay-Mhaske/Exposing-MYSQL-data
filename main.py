from flask import *
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Sujya999$',
    port='3306',
    autocommit=True,
)
mycursor = mydb.cursor()


@app.route('/<string:database>/<string:table>', methods=['GET', 'POST'])
def home(database, table):
    mycursor.execute("USE {}".format(database))
    mycursor.execute("SELECT * FROM {}".format(table))
    data = mycursor.fetchall()
    return data


@app.route('/', methods=['GET', 'POST'])
def index():
    mycursor.execute("SHOW DATABASES")
    data = [i[0] for i in mycursor.fetchall()]
    return render_template('index.html', something=data)


@app.route('/tables', methods=['GET', 'POST'])
def a():
    mycursor.execute("USE {}".format(request.form['choice']))
    mycursor.execute("SHOW TABLES FROM {}".format(request.form['choice']))
    data = [i[0] for i in mycursor.fetchall()]
    return render_template('index2.html', something=data)


@app.route('/tabledata', methods=['GET', 'POST'])
def b():
    mycursor.execute("SELECT * FROM {}".format(request.form['choice']))
    data = mycursor.fetchall()
    return render_template('index3.html', something=data)


if __name__ == '__main__':
    app.run(debug=True)