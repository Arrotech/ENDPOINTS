from flask_restful import Resource
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import OrdersModel
from werkzeug.security import check_password_hash
from app.api.v2.models.users_model import UsersModel
from flask_jwt_extended import create_access_token
from utils.credentials import valid_username, valid_email, valid_password, raise_error
import json


class Register(Resource):
    
    def post(self):

        if not request.json or not 'username' in request.json:
            raise_error(400,"Invalid Key")
        if not request.json or not 'email' in request.json:
            raise_error(400,"Invalid Key")
        if not request.json or not 'password' in request.json:
            raise_error(400,"Invalid Key")


        if type(request.json['username'])not in [str]:
            raise_error(400,"Username should be a string")



        details = request.get_json()

        username = details['username']
        email = details['email']
        password = details['password']
        check_admin = details['check_admin']


        if details["username"]=="":
            raise_error(400,"Username required")
        if details["email"]=="":
            raise_error(400,"Email required")
        if details["password"]=="":
            raise_error(400,"Password required")



        if type(request.json['username'])not in [str]:
            raise_error(400,"Username should be a string")

        if not valid_email(email):
            raise_error(400,"Invalid Username")

        if not valid_password(password):
            raise_error(400,"Invalid Username")

        if not valid_username(username):
            raise_error(400,"Invalid Username")

        if UsersModel().get_username(username):
            raise_error(400,"Username Already Exists")

        if UsersModel().get_email(email):
            raise_error(400,"Email Already Exists")

        user = UsersModel()

        user.save(username, email, password, check_admin)

        return {'message': 'Account created successfully'}, 201


class SignIn(Resource):


    def post(self):

        if not request.json or not 'username' in request.json:
            raise_error(400,"Invalid Key")
        if not request.json or not 'password' in request.json:
            raise_error(400,"Invalid Key")


        if type(request.json['username'])not in [str]:
            raise_error(400,"Username should be a string")

        details = request.get_json()

        user_1 = UsersModel()


        username = details['username']
        password = details['password']


        if details["username"]=="":
            raise_error(400,"Username required")
        if details["password"]=="":
            raise_error(400,"Password required")


        user = user_1.get_username(username)
        
        if user:
            token = create_access_token(identity=username)

            return make_response(jsonify({
                "token" : token
            }), 200)

        if not user:
            return {'message': 'user not found'}, 404

        

        