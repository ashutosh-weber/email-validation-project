from flask import Flask, request, render_template
from mysql.connector import connect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('signup.html')


@app.route('/test', methods=['get'])
def test():
    val1 = request.args.get('email')
    val2 = request.args.get('psw')
    print(val1)
    connection = connect(host="localhost", database="Test", user="root", password="Ashu12345@")
    cur = connection.cursor()

    query1 = "select * from user where email ='{}'".format(val1)
    cur.execute(query1)
    data = cur.fetchone()
    print(data)
    if data == None:

        query = "insert into user values('{}','{}')".format(val1, val2)
        cur.execute(query)
        connection.commit()
    else:
        return render_template('signup.html', error="this email id already signed up")
    return render_template('index.html', email=val1)


@app.route('/login', methods=['get'])
def login():
    email = request.args.get('uname')
    psw = request.args.get('psw')
    connection = connect(host="localhost", database="Test", user="root", password="Ashu12345@")
    cur = connection.cursor()
    query1 = "select password from user where email ='{}'".format(email)
    cur.execute(query1)
    data = cur.fetchone()
    print(data)

    return render_template("login.html")


if __name__ == '__main__':
    app.run()
