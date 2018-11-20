from flask import Flask, Blueprint, request, make_response, jsonify
from flask_restful import Api
from app.api.v2.views.orders_views import DataParcel
from app.manage import UsersDatabase

UsersDatabase().destroy_table()
UsersDatabase().create_table()


parcel_v2 = Blueprint('ors',__name__,url_prefix='/api/v2/')
app_api = Api(parcel_v2)

def parcel_app():


	app = Flask(__name__)

	app.register_blueprint(parcel_v2)
	app_api.add_resource(DataParcel, 'parcels')

	return app