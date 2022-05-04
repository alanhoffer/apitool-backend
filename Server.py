

from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, jwt_required, JWTManager
import json

# DATABASE
from models.Database import db, cursor

# MODELS
from models.Auth import Auth
from models.GroupManager import GroupManager
from models.UserManager import UserManager
from models.ApiaryManager import ApiaryManager
import models.Validate as Validate

#ENTITIES
from models.entities.EUser import EUser
from models.entities.EApiary import EApiary
from models.entities.EGroup import EGroup

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'db9c61ec0aa34ce9cdd3b6705d70d1f1'    
app.config["JWT_SECRET_KEY"] = "db9c61ec0aa35ce9cdd3b6705d70d1f1"

jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": "*"}})

expires = timedelta(days=365)

@app.route('/', methods=['GET', 'POST'])
def index():
    cursor.execute('SELECT * FROM users')
    group = cursor.fetchone()
    return ("Group: " + str(group[0]))


#AUTHENTICATION API
@cross_origin
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        #obtengo los datos del usuario que quiere loguearse
        request_json = request.json
        
        #valido los datos enviados pasandolos a un metodo y los asigno en una variable
        user = Validate.login(request_json)
        
        #si los datos son validos, lo registro en la base de datos
        if user:
            logged_user = Auth.login(user)
            
            #si el usuario existe
            if logged_user != None:
                # y si la contraseña es correcta
                if logged_user.password == True:
                    #genero un token para el usuario
                    access_token = create_access_token(identity=logged_user.userid, expires_delta=expires)
                    #retorno el token
                    response = {"access_token":access_token, "userid":logged_user.userid}
                    return response, 200
                else:
                    return jsonify({"msg": "Wrong password"})
            else:
                return jsonify({"msg": "Wrong username"})
        else:
            return jsonify({"msg": "Invalid data"})
     
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        
        # asigno a una variable el json que envio el post del cliente
        request_json = request.json
        
        #valido los datos enviados pasandolos a un metodo y los asigno en una variable
        user = Validate.register(request_json)
        
        #si los datos son validos, lo registro en la base de datos
        if user:
            registered_user = Auth.register(user)
            
            #si el usuario se registro correctamente, genero un token para el usuario
            if registered_user:
                access_token = create_access_token(identity=registered_user.userid, expires_delta=expires)
                print(registered_user.userid,"id")
                #retorno el token al cliente
                response = {"access_token":access_token,"userid":registered_user.userid}
                return response, 200
            else:
                return jsonify({"msg": "User already exists"})
        else:
            return jsonify({"msg": "Invalid data"})


# FIX LOGOUT IS NOT WORKING ENOUGH
@jwt_required() #new line
@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({'logout': True})
    return response, 200
    
    
#PAGES API
# @cross_origin
# @app.route('/dashboard', methods=['GET'])
# @jwt_required() #new line
# def dashboard():
#     userid = get_jwt_identity()
#     if userid:
#         user = UserManager.get_user_by_id(userid)
#         if user:
#             return jsonify(user)

@cross_origin
@app.route('/token', methods=['GET'])
@jwt_required()
def token():
    if get_jwt_identity():
        print('identity', get_jwt_identity(), 'token', get_jwt())
        return jsonify({"token": True})

@cross_origin
@app.route('/users/<userid>', methods=['GET'])
@jwt_required()
def users(userid):
    if int(userid) == get_jwt_identity():
        user = UserManager.get_user_by_id(userid)
        if user:
            return jsonify(user)
        else:
            return jsonify({"msg": "User not found"})
    else:
        return jsonify({"msg":  "You are not authorized"})




# APIARY API
@cross_origin
@app.route('/users/<userid>/apiaries', methods=['GET'])
@jwt_required()
def apiaries(userid):
    if int(userid) == get_jwt_identity():
        apiaries = ApiaryManager.getApiaries(userid)
        if apiaries:
            return jsonify(apiaries)
        else:
            return jsonify({"msg": "Apiaries not found"})

@cross_origin
@app.route('/createapiary', methods=['GET', 'POST'])
@jwt_required()
def createapiary():
    userid = get_jwt_identity()
    if userid:
        apiary = EApiary(0,request.json['name'],userid)
        if apiary:
            created_apiary = ApiaryManager.createApiary(apiary)
            if created_apiary:
                return jsonify({"msg": "Apiary created"}),200
            else:
                return jsonify({"msg": "Name to short"}),400
            

# GROUPS API
# @cross_origin
# @app.route('/creategroup', methods=['GET', 'POST'])
# @jwt_required()
# def creategroup():
#     userid=get_jwt_identity()
#     group = EGroup(0,request.json['name'])
    
#     groupcreated = GroupManager.createGroup(userid,group)
#     if groupcreated:
#         GroupManager.joinGroup(userid,request.json['name'])
#         return jsonify({"msg": "Group created"}),200
#     else:
#         return jsonify({"msg": "Group already exists"}),400
    


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80",debug=True)
    

