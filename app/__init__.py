from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.api.v2.views.orders_views import DataParcel, GetParcels
from app.api.v2.views.users_views import SignIn, Register


def parcel_app():


	app = Flask(__name__)

	api = Api(app)

	api.add_resource(DataParcel, '/api/v2/parcels')
	api.add_resource(GetParcels, '/api/v2/parcel')
	api.add_resource(Register, '/api/v2/auth/signup')
	api.add_resource(SignIn, '/api/v2/auth/login')

	return app