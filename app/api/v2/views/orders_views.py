from flask_restful import Resource
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import UsersModel
from flask_jwt_extended import jwt_required, get_jwt_identity



class DataParcel(Resource):
    def __init__(self):
        pass 

    @jwt_required
    def post(self):
        if not request.json or not 'sender_name' in request.json:
            abort(400)
        if not request.json or not 'recipient' in request.json:
            abort(400)
        if not request.json or not 'destination' in request.json:
            abort(400)
        if not request.json or not 'pickup' in request.json:
            abort(400)
        if not request.json or not 'weight' in request.json:
            abort(400)
        if not request.json or not 'username' in request.json:
            abort(400)

        if (not request.json or "sender_name" not in request.json):
            return make_response(jsonify({'Error': "Request Not found"}), 404)

        if type(request.json['username'])not in [str]:
            return make_response(jsonify({"Warning!": "Username should be a string"}))


        details = request.get_json()

        sender_name = details['sender_name']
        recipient = details['recipient']
        destination = details['destination']
        pickup = details['pickup']
        weight = details['weight']
        username = details['username']

        if details["sender_name"]=="":
            abort(400)
        if details["recipient"]=="":
            abort(400)
        if details["destination"]=="":
            abort(400)
        if details["pickup"]=="":
            abort(400)
        if details["weight"]=="":
            abort(400)
        if details["username"]=="":
            abort(400)
        
        res = UsersModel().save(sender_name,recipient,destination,pickup,weight,username)
        return make_response(jsonify({
            "Parcel Order": res
            }),201)


    @jwt_required
    def get_parcels(self):
        orders = UsersModel().get_all_parcels()
        if not orders:
            return make_response(jsonify({
                "Message": "Unavailable orders"
            }), 200)
        return make_response(jsonify({
            "Parcel Order": orders
            }),200)

class SingleParcel(Resource):
    
    def get_parcel(parcel_id):
        order = ParcelModel().get_parcel_by_id(parcel_id)
        if not order:
            return make_response(jsonify({
                "Message": "Unavailable order"
            }), 200)
        return make_response(jsonify({
            "Parcel Order": order
            }),200)

    def put(parcel_id):
        order = ParcelModel().cancel_order(parcel_id)
        if not order:
            return make_response(jsonify({
                "Message": "Unavailable order"
            }), 200)
        return jsonify({
            "Status": "Order cancelled",
            "Order" : order
            }), 200

    def get_user(username):
        user = ParcelModel().user_orders_by_username(username)
        if not user:
            return make_response(jsonify({
                "Message": "User does not exist"
            }), 200)
        return jsonify({
            "User" : user
            }), 200

    def delete(parcel_id):
        orders = ParcelModel().get_all_parcels()
        order = [
        order for order in orders if order['parcel_id'] == parcel_id]
        if not order:
            return make_response(jsonify({'Message': "Order Unavailable"}),  400)
        parcel = ParcelModel()
        parcel.delete_order(parcel_id)
        return make_response(jsonify({'Message': "Order deleted"}), 200)



