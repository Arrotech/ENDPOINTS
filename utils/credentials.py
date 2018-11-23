import re
from flask import jsonify, make_response

def check_register_keys(request):

    res_keys = ['email', 'username', 'password', 'check_admin']

    errors = []

    for key in res_keys:
        if not key in request.json:
            errors.append(key)

    return errors

def check_order_keys(request):

    res_keys = ['sender_name', 'recipient', 'pickup', 'destination', 'weight', 'username']

    errors = []

    for key in res_keys:
        if not key in request.json:
            errors.append(key)

    return errors


def check_login_keys(request):

    res_keys = ['username', 'password']

    errors = []

    for key in res_keys:
        if not key in request.json:
            errors.append(key)

    return errors

    

def raise_error(status, msg):
        return make_response(jsonify({
                "status": "error",
                "message": msg
            }), status)

def valid_person_name(customer_name):
    '''validate person's name'''
    regex = "^[a-zA-Z ]{4,}$"
    return re.match(regex, customer_name)


def valid_destination(destination):
    '''validate destination name'''
    regex = "^[a-zA-Z 0-9]{3,}$"
    return re.match(regex, destination)


def valid_username(username):
    ''' validate username '''
    regex = "^[a-zA-Z0-9]{6,20}$"
    return re.match(regex, username)


def valid_password(hash_password):
    '''validate password , min of 6 chars'''
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{6,}$"
    return re.match(regex, hash_password)


def valid_email(email):
    ''' validate email '''
    regex = "^[^@]+@[^@]+\.[^@]+$"
    return re.match(regex, email)
