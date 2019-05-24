user_register = {
"email": "janie@gmail.com",
"password": "20930988",
"username": "janie",
"admin": "False"
}

new_register = {
"email": "miriam@gmail.com",
"password": "20930988",
"username": "miriam",
"admin": "False"
}

wrong_register_keys = {
"eml": "janie@gmail.com",
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

wrong_format_sender = {
"sender_name": "Joh n",
"recipient": "Kevin",
"pickup": "racecourse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

wrong_format_recepient = {
"sender_name": "John",
"recipient": "Kev $2n",
"pickup": "racecourse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

wrong_format_pickup = {
"sender_name": "John",
"recipient": "Kevin",
"pickup": "raceco 37  urse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

wrong_format_destination = {
"sender_name": "John",
"recipient": "Kevin",
"pickup": "racecourse",
"destination": "Dub45 ai",
"weight": 2,
"username": "ogol",
"order_status": "Delivered"
}

wrong_format_username = {
"sender_name": "John",
"recipient": "Kevin",
"pickup": "racecourse",
"destination": "Dubai",
"weight": 2,
"username": "o 436 gol",
"order_status": "Delivered"
}

wrong_format_order = {
"sender_name": "John",
"recipient": "Kevin",
"pickup": "racecourse",
"destination": "Dubai",
"weight": 2,
"username": "ogol",
"order_status": "D  537elivered"
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

correct_pickup = {
"id": 1,
"pickup": "jkuat"
}

wrong_pickup_key = {
"piCkup": "jkuat"
}

wrong_pickup_value = {
"pickup": "  !2@mombasa"
}

correct_destination = {
"id": 1,
"destination": "meru"
}

wrong_destination_key2 = {
"destnation": "jkuat"
}

wrong_destination_key_value = {
"destination": "jku 614at"
}

correct_order_status = {
"id": 1,
"order_status": "meru"
}

wrong_order_status_key = {
"ordertatus": "jkuat"
}

wrong_order_status_value = {
"order_status": "jku 614at"
}
