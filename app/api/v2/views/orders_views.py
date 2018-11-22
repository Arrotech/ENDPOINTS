from flask_restful import Resource
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import OrdersModel
from utils.credentials import raise_error


class DataParcel(Resource):
    """Creates a new order."""
    
    def post(self):

        res_keys = ['sender_name', 'recipient', 'destination', 'pickup', 'weight', 'username']

        for key in res_keys:
            if key is not request.json:
                return raise_error(400,"Invalid {}".format(key))


        if type(request.json['username'])not in [str]:
            raise_error(400,"Username should be a string")

        details = request.get_json()

        sender_name = details['sender_name']
        recipient = details['recipient']
        destination = details['destination']
        pickup = details['pickup']
        weight = details['weight']
        username = details['username']

        if details["sender_name"]=="":
            raise_error(400,"Invalid Key")
        if details["recipient"]=="":
            raise_error(400,"Invalid Key")
        if details["destination"]=="":
            raise_error(400,"Invalid Key")
        if details["pickup"]=="":
            raise_error(400,"Invalid Key")
        if details["weight"]=="":
            raise_error(400,"Invalid Key")
        if details["username"]=="":
            raise_error(400,"Invalid Key")
        
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
            "Parcel Order" : order
            }),200)


class Destination(Resource):
    """Change order destination."""


    def put(self, parcel_id):

        details = request.get_json()
        
        destination = details['destination']

        order = OrdersModel().change_destination(destination,parcel_id)
        if order:
            return jsonify({
                "destination" : order
                })


'''class DeleteOrder(Resource):
    """Delete specific order."""


    def delete(self, parcel_id):
        orders = OrdersModel().get_all_parcels()
        order = [
        order for order in orders if order['parcel_id'] == parcel_id]
        if not order:
            return make_response(jsonify({'message': "Order Unavailable"}),  404)
        parcel = OrdersModel()
        parcel.delete_order(parcel_id)
        return make_response(jsonify({'message': "Order deleted"}), 200)


class CancelOrder(Resource):
    """Cancel specific order."""


    def put(self, parcel_id):
        order = OrdersModel().cancel_order(parcel_id)
        if order:
            return jsonify({
                "Status": "Order cancelled",
                "Order" : order
                }), 200
        return make_response(jsonify({
                "Message": "Order Not Found"
            }), 404)'''

    

    
    



