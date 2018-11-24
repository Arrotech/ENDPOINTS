from flask_restful import Resource
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import OrdersModel
from werkzeug.security import check_password_hash, generate_password_hash
from app.api.v2.models.users_model import UsersModel
from flask_jwt_extended import create_access_token
from utils.credentials import is_valid_email, is_valid_numbers, is_valid_username, raise_error, check_register_keys, check_login_keys
import json



                

class Register(Resource):
    
    def post(self):
        """Create new account."""

        details = request.get_json()

        errors = check_register_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        if details['username'].isalpha()== False:
            return {"Status": "username is in wrong format"}
        if details["username"]=="":
            raise_error(400,"Username required")
        if details["email"]=="":
            raise_error(400,"Email required")
        if details["password"]=="":
            raise_error(400,"Password required")
        if type(request.json['username'])not in [str]:
            return {"message": "Invalid username"}

        username = details['username']
        email = details['email']
        password = generate_password_hash(details['password'])
        admin = details['admin']
        
        if not is_valid_email(email):
            return {"message": "Invalid email or Password"}
        if UsersModel().get_username(username):
            return {"message": "Username Already Exists"}
        if UsersModel().get_email(email):
            return {"message": "Email Already Exists"}

        user = UsersModel()
        user.save(username, email, password, admin)
        return {'message': 'Account created successfully'}, 201


class SignIn(Resource):


    def post(self):
        """Sign In a user"""

        errors = check_login_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))


        if type(request.json['username'])not in [str]:
            raise_error(400,"Username should be a string")

        details = request.get_json()

        username = details['username']
        password = details['password']

        if details["username"]=="":
            raise_error(400,"Username required")
        if details["password"]=="":
            raise_error(400,"Password required")


        user_1 = UsersModel()
        user = user_1.get_username(username)


        if user:
            token = create_access_token(identity=username)
            return make_response(jsonify({
                "message" : "successfully logged in",
                "token" : token
            }), 200)
        if not user:
            return {'message': 'user not found'}, 404

        

        