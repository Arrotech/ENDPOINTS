from flask import Flask, Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from app.api.v2.views.orders_views import DataParcel, GetParcels, GetParcel, Destination, PresentLocation, ChangeStatus
from app.api.v2.views.users_views import SignIn, Register
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from app.config import app_config


def page_not_found(e):
	"""Capture Not Found error"""

	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
		}), 404)


def parcel_app(config_name):
	"""Create app """

	app = Flask(__name__)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config["JWT_SECRET_KEY"] = 'thisisarrotech'
	jwt = JWTManager(app)
	api = Api(app)
	api.add_resource(DataParcel, '/api/v2/parcels')
	api.add_resource(GetParcels, '/api/v2/parcels')
	api.add_resource(GetParcel, '/api/v2/parcels/<int:parcel_id>')
	api.add_resource(Destination, '/api/v2/parcels/<int:parcel_id>/destination')
	api.add_resource(PresentLocation, '/api/v2/parcels/<int:parcel_id>/location')
	api.add_resource(ChangeStatus, '/api/v2/parcels/<int:parcel_id>/status')
	api.add_resource(Register, '/api/v2/auth/signup')
	api.add_resource(SignIn, '/api/v2/auth/login')
	app.register_error_handler(404, page_not_found)
	
	return app