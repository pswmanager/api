from flask import Flask, request
from controller import get_passwords, get_users, post_passwords, post_users, put_passwords, delete_passwords
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == "GET":
        return get_users(request)
    elif request.method == 'POST':
        return post_users(request)


@app.route("/passwords", methods=['GET', 'POST', 'PUT', 'DELETE'])
def offerte():
    if request.method == 'GET':
        return get_passwords(request)
    elif request.method == 'POST':
        return post_passwords(request)
    elif request.method == "PUT":
        return put_passwords(request)
    elif request.method == "DELETE":
        return delete_passwords(request)
    

app.run(debug=True, port=2000)