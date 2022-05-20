
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, jwt_required, JWTManager
from flask import Flask, jsonify, request


@jwt_required()
def token():
    if get_jwt_identity():
        return jsonify({"token": True}), 200
