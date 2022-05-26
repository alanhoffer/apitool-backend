

from datetime import timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, jwt_required, JWTManager



# MODELS2
from models.Auth import Auth
from models.GroupManager import GroupManager
from models.NoticeManager import NoticeManager
from models.UserManager import UserManager
from models.ApiaryManager import ApiaryManager
import models.Validate as Validate
from models.entities.EApiaryConfig import EApiaryConfig
from models.entities.ENotice import ENotice

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




#AUTHENTICATION API


@cross_origin
@app.route('/login', methods=['POST'])
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
                    print(response)
                    return response, 200
                else:
                    return jsonify({"msg": "Wrong password"}), 401
            else:
                return jsonify({"msg": "Wrong username"}), 401
        else:
            return jsonify({"msg": "Invalid data"}), 401
        
        
        
     
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
                return jsonify({"msg": "User already exists"}), 401
        else:
            return jsonify({"msg": "Invalid data"}), 401


# FIX LOGOUT IS NOT WORKING ENOUGH
@jwt_required() #new line
@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({'logout': True})
    return response, 200
    

@cross_origin
@app.route('/token', methods=['GET'])
@jwt_required()
def token():
    if get_jwt_identity():
        return jsonify({"token": True}), 200




#USER API
@cross_origin
@app.route('/users/<userid>', methods=['GET'])
@jwt_required()
def users(userid):
    if int(userid) == get_jwt_identity():
        user = UserManager.get_user_by_id(userid)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"msg": "User not found"}), 404
    else:
        return jsonify({"msg":  "You are not authorized"}), 401 
        
@cross_origin
@app.route('/users/<userid>', methods=['PUT'])
@jwt_required()
def users_update(userid):
    if int(userid) == get_jwt_identity():
        user = UserManager.get_user_by_id(userid)
        if user:
            request_json = request.json
            user = Validate.update_user(request_json, user)
            if user:
                user = UserManager.update_user(user)
                if user:
                    return jsonify(user), 200
                else:
                    return jsonify({"msg": "User not found"}), 404
            else:
                return jsonify({"msg": "Invalid data"}), 401
        else:
            return jsonify({"msg": "User not found"}), 404



# APIARY API
@cross_origin
@app.route('/apiaries', methods=['GET'])
@jwt_required()
def apiaries():
    userid = get_jwt_identity()
    if userid:
        apiaries = ApiaryManager.getApiaries(userid)
        if apiaries:
            return jsonify(apiaries), 200
        else:
            return jsonify({"msg":  "Dont have apiaries"}), 400 
    else:
        return jsonify({"msg":  "You are not authorized"}), 401

@cross_origin
@app.route('/apiaries', methods=['POST'])
@jwt_required()
def createapiary():
    userid = get_jwt_identity()
    
    if userid:
        response_apiary = request.json['apiary']
        response_config = request.json['config']
        apiary = EApiary(0, userid, response_apiary['name'])
        if apiary:
            created_apiary = ApiaryManager.createApiary(apiary)
            if created_apiary:
                apiary_config = EApiaryConfig(0, created_apiary, response_config)
                ApiaryManager.createApiaryConfig(apiary_config)
                return jsonify({"msg": "Apiary created"}),200
            else:
                return jsonify({"msg": "Error at creating apiary"}),400
        else:
            return jsonify({"msg": "Invalid data"}),401
    else:
        return jsonify({"msg":  "You are not authorized"}), 401
            # response_config['hive_quantity'], response_config['hive_quantity'], response_config['apiary_food_quantity'], response_config['apiary_note_record'],response_config['apiary_electric_protection'],response_config['apiary_status'],response_config['health_flumetrine'],response_config['apiary_note_record'],response_config['apiary_note_record'], )
@cross_origin
@app.route('/apiaries/<apiaryid>', methods=['GET'])
@jwt_required()
def apiary(apiaryid):
    if int(apiaryid) == get_jwt_identity():
        apiary = ApiaryManager.getApiary(apiaryid)
        if apiary:
            return jsonify(apiary), 200
        else:
            return jsonify({"msg":  "You are not authorized"}), 401
        
@cross_origin
@app.route('/apiaries/<apiaryid>', methods=['PUT'])
@jwt_required()
def updateapiary(apiaryid):
    if int(apiaryid) == get_jwt_identity():
        apiary = ApiaryManager.getApiary(apiaryid)
        if apiary:
            updated_apiary = ApiaryManager.updateApiary(apiary,request.json['name'])
            if updated_apiary:
                return jsonify({"msg": "Apiary updated"}),200
            else:
                return jsonify({"msg": "Error at updating apiary"}),400


@cross_origin
@app.route('/apiaries/<apiaryid>', methods=['DELETE'])
@jwt_required()
def deleteapiary(apiaryid):
    if int(apiaryid) == get_jwt_identity():
        apiary = ApiaryManager.getApiary(apiaryid)
        if apiary:
            deleted_apiary = ApiaryManager.deleteApiary(apiary)
            if deleted_apiary:
                return jsonify({"msg": "Apiary deleted"}),200
            else:
                return jsonify({"msg": "Error at deleting apiary"}),400
            

#NOTICES API
@cross_origin
@app.route('/notice', methods=['GET'])
@jwt_required()
def notice():
    userid = get_jwt_identity()
    if userid:
        notices = NoticeManager.getAll()
        if notices:
            return jsonify(notices), 200
        else:
            return jsonify({"msg": "Notices not found"}),404
    else:
        return jsonify({"msg": "You are not authorized"}), 401
    
@cross_origin
@app.route('/notice/<id>', methods=['GET'])
@jwt_required()
def noticeGet(id):
    userid = get_jwt_identity()
    if userid:
        notice = NoticeManager.getById(id)
        if notice:
            return jsonify(notice), 200
        else:
            return jsonify({"msg": "Notice not found"}),404
    
@cross_origin
@app.route('/notice', methods=['POST'])
@jwt_required()
def noticeCreate():

    notice = ENotice(0,request.json['title'],request.json['text'], request.json['img'])
    if notice:
        created_notice = NoticeManager.create(notice)
        if created_notice:
            return jsonify({"msg": "Notice created"}),200
        else:
            return jsonify({"msg": "notice lenght is bad"}),400
    else:
        return jsonify({"msg": "Invalid data"}),400

        
@cross_origin
@app.route('/notice/<id>', methods=['PUT'])
@jwt_required()
def noticeUpdate(id):
    userid = get_jwt_identity()
    if userid:
        notice = NoticeManager.getById(id)
        if notice:
            notice.title = request.json['title']
            notice.text = request.json['text']
            notice.img = request.json['img']
            updated_notice = NoticeManager.update(notice)
            if updated_notice:
                return jsonify({"msg": "Notice updated"}),200
            else:
                return jsonify({"msg": "Notice not updated"}),400
        else:
            return jsonify({"msg": "Notice not found"}),404
            
            
@cross_origin
@app.route('/notice/<id>', methods=['DELETE'])
@jwt_required()
def noticeDelete(id):
    userid = get_jwt_identity()
    if userid:
        notice = NoticeManager.getById(id)
        if notice:
            deleted_notice = NoticeManager.delete(id)
            print("noticee",deleted_notice)
            if deleted_notice:
                return jsonify({"msg": "Notice deleted"}),200
            else:
                return jsonify({"msg": "Notice not deleted"}),400
    else:
        return jsonify({"msg": "You are not authorized"}), 401
    
        

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80",debug=True)
    

