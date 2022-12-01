from flask import request
import mysql.connector
from models.id import ID
import json

USER = "admin"
PASSWORD = "G!getto2004"

db = mysql.connector.connect(
    host='pswmanagerdb.c4n1igd3jeuj.eu-west-2.rds.amazonaws.com',
    user=USER,
    passwd=PASSWORD,
    database='pswmanagerdb'
)

def get_users(request):
    try:
        username = request.args['username']

        password = request.args['password']

        with open("autenticate.sql", 'r') as f:
            query = f.readline()
        
        cursor = db.cursor()

        cursor.execute(query, (username, password,))

        selected_id = None

        for id in cursor:
            selected_id = ID(id)
            break

        return {"id": selected_id.id}
    
    except:
        return {"Error": "user not found"}

def post_users(request):
    try:
        dict = json.loads(request.data)

        print(dict)

        with open("insert-user.sql", 'r') as f:
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
        user_id = request.args["user_id"]

        with open('select-passwords.sql', 'r') as f:
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

        return values
    except:
        return {"Error": True}

def post_passwords(request):
    try:
        data = json.loads(request.data)

        with open('insert-passwords.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (data["platform"], data["username"], data["password"], data["user_id"],))

        db.commit()

        return data
    except:
        return {"Error": True}

def put_passwords(request):
    try:
        data = json.loads(request.data)

        with open('update-password.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (data["password"], data["id"],))

        db.commit()   

        return data
    
    except:

        return {"Error": True}

def delete_passwords(request):
    try:
        id = request.args["id"]

        with open('delete-password.sql', 'r') as f:
            query = f.readline()

        cursor = db.cursor()

        cursor.execute(query, (id,))

        db.commit()   

        return {"Error": False}
    
    except:

        return {"Error": True}
