from flask import request
import mysql.connector
from models.id import ID
import json

USER = "gabrielefurlan"
PASSWORD = "nuovapass"

def get_users(request):
    try:
        db = mysql.connector.connect(
            host='gabrielefurlan.mysql.pythonanywhere-services.com',
            user=USER,
            passwd=PASSWORD,
            database='gabrielefurlan$pswmanager'
        )

        username = request.args['username']

        password = request.args['password']

        with open("/home/gabrielefurlan/pswmanager/autenticate.sql", 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (username, password,))

        selected_id = None

        for id in cursor:
            selected_id = ID(id)
            break

        return {"id": selected_id.id}

    except:

        return {"Error": True}


def post_users(request):
    try:
        db = mysql.connector.connect(
            host='gabrielefurlan.mysql.pythonanywhere-services.com',
            user=USER,
            passwd=PASSWORD,
            database='gabrielefurlan$pswmanager'
        )

        dict = json.loads(request.data)

        username = dict['username']


        with open("/home/gabrielefurlan/pswmanager/usernameavailable.sql", 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (username,))

        print(cursor)

        for val in cursor:
            if val[0] != 0:
                return {"Error": "username in use"}
            break

        with open("/home/gabrielefurlan/pswmanager/insert-user.sql", 'r') as f:
            query = f.readline()

        print(query)

        cursor = db.cursor()

        res = cursor.execute(query, (dict["username"], dict["password"], dict["email"],))

        print("query eseguita")

        db.commit()

        print(res)

        return dict

    except:

        return {"Error": True}

def get_passwords(request):
    try:
        db = mysql.connector.connect(
            host='gabrielefurlan.mysql.pythonanywhere-services.com',
            user=USER,
            passwd=PASSWORD,
            database='gabrielefurlan$pswmanager'
        )

        user_id = request.args["user_id"]

        with open('/home/gabrielefurlan/pswmanager/select-passwords.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        res = cursor.execute(query, (user_id,))

        values = list()

        for val in cursor:
            values.append({
                "id": val[0],
                "platform": val[1],
                "username": val[2],
                "password": val[3],
                "user_id": val[4]
            })

        return json.dumps(values)
    except:
        return {"Error": True}

def post_passwords(request):
    try:
        db = mysql.connector.connect(
            host='gabrielefurlan.mysql.pythonanywhere-services.com',
            user=USER,
            passwd=PASSWORD,
            database='gabrielefurlan$pswmanager'
        )

        data = json.loads(request.data)

        with open('/home/gabrielefurlan/pswmanager/insert-passwords.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (data["platform"], data["username"], data["password"], data["user_id"],))

        db.commit()

        return json.dumps(data)
    except:
        return {"Error": True}

def put_passwords(request):
    try:
        db = mysql.connector.connect(
            host='gabrielefurlan.mysql.pythonanywhere-services.com',
            user=USER,
            passwd=PASSWORD,
            database='gabrielefurlan$pswmanager'
        )

        data = json.loads(request.data)

        with open('/home/gabrielefurlan/pswmanager/update-password.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (data["password"], data["id"],))

        db.commit()

        return json.dumps(data)

    except:

        return {"Error": True}

def delete_passwords(request):
    try:
        db = mysql.connector.connect(
            host='gabrielefurlan.mysql.pythonanywhere-services.com',
            user=USER,
            passwd=PASSWORD,
            database='gabrielefurlan$pswmanager'
        )

        id = request.args["id"]

        with open('/home/gabrielefurlan/pswmanager/delete-password.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (id,))

        db.commit()

        return {"Error": False}

    except:

        return {"Error": True}