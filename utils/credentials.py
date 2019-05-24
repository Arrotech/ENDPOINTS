import re
from flask import jsonify, make_response

def check_register_keys(request):

    res_keys = ['email', 'username', 'password']
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

def raise_error(status, msg):
        return make_response(jsonify({
                "status": "error",
                "message": msg
            }), status)

def is_valid_email(variable):
   """Check if email is a valid mail."""
   if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
               variable):
       return True
   return False

def is_valid_password(variable):
   """Check if password is a valid password."""
   if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', variable):
       return True
   return False

def is_valid_username(variable):
   """Check if username is a valid username."""
   if re.match(r'[A-Za-z$]', variable):
       return True
   return False

