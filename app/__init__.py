from flask import Flask, Blueprint, request, make_response, jsonify
from flask_restful import Api
from app.api.v2.views.orders_views import DataParcel, SingleParcel
from app.api.v2.views.users_views import Register, SignIn
from flask_jwt_extended import JWTManager


from app.manage import UsersDatabase

UsersDatabase().destroy_table()
UsersDatabase().create_table()

jwt = JWTManager()

parcel_v2 = Blueprint('orders',__name__,url_prefix='/api/v2')


app_api = Api(parcel_v2)

def parcel_app():
	app = Flask(__name__)
	jwt.init_app(app)

	app.register_blueprint(parcel_v2)


	
	app_api.add_resource(Register, '/auth/signup')
	app_api.add_resource(SignIn, '/auth/login')
	app_api.add_resource(DataParcel, '/parcels')
	app_api.add_resource(SingleParcel, '/parcels/<int:parcel_id>/destination')
	app_api.add_resource(DataParcel, '/parcels/<int:parcel_id>/present-loacation')

	return app