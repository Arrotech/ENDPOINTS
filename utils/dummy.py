user_register = {
"email": "janie@gmail.com",
"password": "20930988",
"username": "janie",
"admin": "False"
}

email_exists = {
"email": "janie@gmail.com",
"password": "janiedoe20930988",
"username": "janiedoe",
"admin": "False"
}

username_exists = {
"email": "janiedoe@gmail.com",
"password": "johndoe20930988",
"username": "janie",
"admin": "False"
}

user_login = {
"password": "20930988",
"username": "janie"
}

login_unexisting_user = {
"password": "george20930988",
"username": "george"
}

new_user = {
"email": "pmc@gmail.com",
"password": "pmc20930988",
"username": "mary",
"admin": "False"
}

invalid_password = {
"email": "javan@gmail.com",
"password": "",
"username": "javan",
"admin": "False"
}

invalid_email = {
"email": "enosgmail.com",
"password": "20930988!",
"username": "enos",
"admin": "False"
}

create_order = {
"sender_name": "John",
"recipient": "Kevin",
"pickup": "racecourse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

wrong_key_data = {
"senderName": "John",
"recipient": "Kevin",
"pickup": "racecourse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

wrong_value_data = {
"sender_name": "John",
"recipient": "Kevin",
"pickup": "race#$  ourse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

get_order = {
"sender_name": "jkuat",
"recipient": "mambo",
"pickup": "nyeri",
"destination": "mitunguu",
"weight": 2,
"username": "njosh",
"order_status": "Delivered"
}

wrong_pickup_key = {
"piCkup": "jkuat"
}

wrong_pickup_value = {
"pickup": "  !2@mombasa"
}

wrong_destination_key = {
"destnation": "jkuat"
}

wrong_destination_value = {
"destination": "basa "
}
