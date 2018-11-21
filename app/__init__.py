from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from app.api.v2.views.orders_views import DataParcel
from app.api.v2.views.users_views import SignIn, Register
from app.api.v2.views.orders_views import parcel_v2 as v2





def parcel_app():


	app = Flask(__name__)

	app.register_blueprint(v2, url_prefix='/api/v2/')

	
	'''app_api.add_resource(DataParcel, 'parcels')
	app_api.add_resource(SingleParcel, 'parcels/<int:parcel_id>')
	app_api.add_resource(SignIn, 'auth/login')
	app_api.add_resource(Register, 'auth/signup')'''

	return app