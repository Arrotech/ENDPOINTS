from flask_restful import Resource
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import OrdersModel
from utils.credentials import raise_error, check_order_keys


class DataParcel(Resource):
    """Creates a new order."""
    
    def post(self):

        details = request.get_json()

        errors = check_order_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))

            
        if type(request.json['username'])not in [str]:
            raise_error(400,"Username should be a string")
        

        sender_name = details['sender_name']
        recipient = details['recipient']
        destination = details['destination']
        pickup = details['pickup']
        weight = details['weight']
        username = details['username']


        if details['sender_name'].isalpha()== False:
            return {"Status": "sender_name is in wrong format"}

        if details['recipient'].isalpha()== False:
            return {"Status": "recipient is in wrong format"}

        if details['pickup'].isalpha()== False:
            return {"Status": "pickup is in wrong format"}

        if details['destination'].isalpha()== False:
            return {"Status": "destination is is wrong format"}

        if details['username'].isalpha()== False:
            return {"Status": "username is in wrong format"}

        
        res = OrdersModel().save(sender_name, recipient, destination, pickup, weight, username)
        return make_response(jsonify({
                "message" : "Order created successfully!"
            }),201)


class GetParcels(Resource):
    """Fetch all orders."""
    
    def get(self):
        orders = OrdersModel().get_all_parcels()
        orders = json.loads(orders)
        if orders:
            return make_response(jsonify({
                "message": "success",
                "Parcel Order": orders
            }),200)
        


class GetParcel(Resource):
    """Fetch a specific order."""


    def get(self, parcel_id):
        order = OrdersModel().get_parcel_by_id(parcel_id)
        order = json.loads(order)
        if order:
            return make_response(jsonify({
            "message": "success",
            "Parcel Order" : order
            }),200)


class Destination(Resource):
    """Change order destination."""


    def put(self, parcel_id):

        details = request.get_json()

        destination = details['destination'].isalpha()

        order = OrdersModel().change_destination(destination,parcel_id)
        if order:
            return jsonify({
                "destination" : order
                })

class PresentLocation(Resource):
    """Change order destination."""


    def put(self, parcel_id):

        details = request.get_json()

        pickup = details['pickup'].isalpha()

        order = OrdersModel().change_present_location(pickup,parcel_id)
        if order:
            return jsonify({
                "pickup" : order
                })



    

    
    



