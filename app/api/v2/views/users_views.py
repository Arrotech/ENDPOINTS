from flask_restful import Resource
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import UsersModel
from werkzeug.security import check_password_hash
from app.api.v2.models.order_models import UsersModel
from flask_jwt_extended import create_access_token
from app.credentials import valid_username, valid_email, valid_password


class Register(Resource):

    def post(self):

        details = request.get_json()

        username = details['username']
        email = details['email']
        password = details['password']

        if not valid_username(username):
            return {'message': 'Invalid username'}, 400

        if not valid_email(email):
            return {'message': 'Invalid email'}, 400

        if not valid_password(password):
            return {'message': 'Invalid password'}, 400

        if not valid_username(username):
            return {'message': 'Invalid username'}, 400

        if UsersModel().get_user_by_username(username):
            return {'message': 'username already in use'}, 400

        if UsersModel().get_user_by_email(email):
            return {'message': 'email already in use'}, 400

        user = UsersModel()

        user.save(username, email, password)

        return {'message': 'Account created successfully'}, 201


class SignIn(Resource):

    def post(self):

        details = request.get_json()

        username = details['username']
        password = details['password']

        user = UsersModel().get_username(username)
        print(user)

        if not user:
            return {'message': 'user not found'}, 404

        if not check_password_hash(user.password, password):
            return {'message': 'Wrong password'}, 400

        token = create_access_token(user.username)
        return {
            'token': token,
            'message': f'You were successfully logged in {username}'
        }, 200
