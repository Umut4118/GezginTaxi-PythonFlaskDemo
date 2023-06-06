import folium
import location as location
from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb
from pymongo import MongoClient
import pprint
import re
import zmq

temp1 = 0
temp2 = 0
tempclock = 0



pp = pprint.PrettyPrinter(indent=4)
try:
    cluster = MongoClient(
        "mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car1']
    print("bağlantı kuruldu")
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car1 = element
Car1list = list(Car1.values())
Car1str = ''.join(map(str, Car1list))
Car1str = re.split('\n|,| ', Car1str)
Car1str[0] = "2018-10-02"
# print(Car1str[0])

try:
    cluster = MongoClient(
        "mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car2']
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car2 = element
Car2list = list(Car2.values())
Car2str = ''.join(map(str, Car2list))
Car2str = re.split('\n|,| ', Car2str)
Car2str[0] = "2018-10-02"
# print(Car2str[1])
try:
    cluster = MongoClient(
        "mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car3']
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car3 = element
Car3list = list(Car3.values())
Car3str = ''.join(map(str, Car3list))
Car3str = re.split('\n|,| ', Car3str)
Car3str[0] = "2018-10-02"
# print(Car3str[2])
try:
    cluster = MongoClient(
        "mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car4']
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car4 = element
Car4list = list(Car4.values())
Car4str = ''.join(map(str, Car4list))
Car4str = re.split('\n|,| ', Car4str)
Car4str[0] = "2018-10-02"
# print(Car4str[3])


app = Flask(__name__)
app.secret_key = "1234353234"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Umut*1234"
app.config["MYSQL_DB"] = "logininfo"
db = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM users WHERE  username=%s AND password=%s ", (username, password))
            info = cursor.fetchone()
            if info is not None:
                if info['username'] == username and info['password'] == password:
                    return render_template("Main.html")
                else:
                    return "fail"
    return render_template("Login.html")


@app.route('/main', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if 'Clock' in request.form:

           temp1=request.form['Clock']
           for i in range (0,len(Car1str)):
            if temp1==Car1str[i]:
             tempclock=i
             return render_template('Map.html')
    return  render_template(('Main.html'))


@app.route('/map', methods=['GET', 'POST'])
def base():
    map = folium.Map(
        location=[59, 18],
        zoom_start=12
    )
    for i in range(2,len(Car1str),5):
        folium.Marker(
            location=[Car1str[i], Car1str[i + 1]],
            popup="<i>Marker here</i>",

        ).add_to(map)

    return map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
