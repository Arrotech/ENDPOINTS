from flask_restful import Resource
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.order_models import OrdersModel
from app.api.v2.models.users_model import UsersModel
from utils.credentials import check_order_status_keys, raise_error, check_pickup_keys, check_order_keys, check_destination_keys
from flask_jwt_extended import jwt_required, get_jwt_identity

class DataParcel(Resource):
    """Creates a new order."""

    @jwt_required
    def post(self):



        details = request.get_json()

        errors = check_order_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))

        sender_name = details['sender_name']
        recipient = details['recipient']
        destination = details['destination']
        pickup = details['pickup']
        weight = details['weight']
        username = details['username']
        order_status = details['order_status']

        if details['sender_name'].isalpha()== False:
            return make_response(jsonify({"message": "sender_name is in wrong format"}),400)
        if details['recipient'].isalpha()== False:
            return make_response(jsonify({"message": "recipient is in wrong format"}),400)
        if details['pickup'].isalpha()== False:
            return make_response(jsonify({"message": "pickup is in wrong format"}),400)
        if details['destination'].isalpha()== False:
            return make_response(jsonify({"message": "destination is in wrong format"}),400)
        if details['username'].isalpha()== False:
            return make_response(jsonify({"message": "username is in wrong format"}),400)
        if details['order_status'].isalpha()== False:
            return make_response(jsonify({"message": "Order status is in wrong format"}),400)
        """user = UsersModel().get_username(username)
        if user.admin == True:"""
        res = OrdersModel().save(sender_name, recipient, destination, pickup, weight, username, order_status)
        return make_response(jsonify({
                "message" : "Order created successfully!"
            }),201)

        """return {"message": "Not authorized"}"""


class GetParcels(Resource):
    """Fetch all orders."""

    @jwt_required
    def get(self):

        return make_response(jsonify({
            "message": "success",
            "Parcel Order": json.loads(OrdersModel().get_all_parcels())
        }),200)


class GetParcel(Resource):
    """Fetch a specific order."""

    @jwt_required
    def get(self, parcel_id):
        order = OrdersModel().get_parcel_by_id(parcel_id)
        order = json.loads(order)
        if order:
            return make_response(jsonify({
            "message": "success",
            "Parcel Order" : order
            }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "order not found"
        }), 404)


class Destination(Resource):
    """Change order destination."""

    @jwt_required
    def put(self, parcel_id):

        errors = check_destination_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        destination = details['destination']
        if details['destination'].isalpha()== False:
            return make_response(jsonify({"message": "destination is in wrong format"}),400)
        order = OrdersModel().change_destination(destination,parcel_id)
        if order:
            return make_response(jsonify({
                "message" : "successfully changed the destination"
                }), 201)

class PresentLocation(Resource):
    """Change order destination."""

    @jwt_required
    def put(self, parcel_id):
        """Admin can change present location"""

        errors = check_pickup_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        if details['pickup'].isalpha()== False:
            return make_response(jsonify({"message": "pickup is in wrong format"}),400)
        pickup = details['pickup']
        order = OrdersModel().change_present_location(pickup,parcel_id)
        if order:
            return make_response(jsonify({
                "message" : "successfully changed the current location"
                }), 201)

class ChangeStatus(Resource):

    @jwt_required
    def put(self, parcel_id):
        """Change status."""

        errors = check_order_status_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        if details['order_status'].isalpha()== False:
            return make_response(jsonify({"message": "Order status is in wrong format"}),400)
        order_status = details['order_status']
        order = OrdersModel().change_status(order_status,parcel_id)
        if order:
            return make_response(jsonify({
                "message" : "successfully changed the status"
                }), 201)
