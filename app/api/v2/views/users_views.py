from flask_restful import Resource
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import OrdersModel
from werkzeug.security import check_password_hash, generate_password_hash
from app.api.v2.models.users_model import UsersModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utils.credentials import is_valid_email, is_valid_username, raise_error, check_register_keys #is_valid_password,
import json


class Register(Resource):

    def post(self):
        """Create new account."""

        details = request.get_json()

        errors = check_register_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))

        username = details['username']
        email = details['email']
        password = generate_password_hash(details['password'])
        admin = False

        if not is_valid_email(email):
            return {"message": "Invalid Email"}
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

        details = request.get_json()

        username = details['username']
        password = details['password']

        user = UsersModel().get_username(username)

        if user:
            token = create_access_token(identity=username)
            return make_response(jsonify({
                "message" : f"successfully logged in {username}",
                "token" : token
            }), 200)
        if not user:
            return {'message': 'user not found'}, 404

class User(Resource):
    """Fetch orders by a single user"""

    @jwt_required
    def get(self, username):
        """Admin can fetch a single user"""

        user = UsersModel().get_username(username)
        """orders = json.loads(orders)"""
        if user:
            return make_response(jsonify({
                "message": "success",
                "user": user
                }), 200)
        return make_response(jsonify({
            "message": "user not found"
            }), 404)

class Users(Resource):
    """Admin can fetch all users"""

    @jwt_required
    def get(self):
        return make_response(jsonify({
            "message": "success",
            "Users": json.loads(UsersModel().get_users())
            }), 200)
