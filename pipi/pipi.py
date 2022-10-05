from sqlite3 import Date
from flask import Flask, jsonify, request, json

app = Flask(__name__)


db_users = []

@app.route("/")
def hello_world():
    return "<p>Перейди в Postman</p>"



 # http://127.0.0.1:5000/user
@app.route("/user", methods = ['post', 'get'])
def create():
    if request.method == 'GET':
        return db_users, 200
    if request.method == 'POST':
        date = request.json
        if(date== False and []):
            return "Данные не заполнены", 403
        if (date ["name"] ==''):
            return "Поле имя не заполнено", 403

        db_users.append(date["name"])
        db_users.append(date["email"])
        db_users.append(date["password"])

        return "Пользователь добавлен", 200
    
    return jsonify (date)   



