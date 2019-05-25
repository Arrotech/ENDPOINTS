

[![Build Status](https://travis-ci.org/Arrotech/ENDPOINTS.svg?branch=develop)](https://travis-ci.org/Arrotech/ENDPOINTS) [![Maintainability](https://api.codeclimate.com/v1/badges/c497d0de46c8d2767806/maintainability)](https://codeclimate.com/github/Arrotech/ENDPOINTS/maintainability) [![Coverage Status](https://coveralls.io/repos/github/Arrotech/ENDPOINTS/badge.svg?branch=develop)](https://coveralls.io/github/Arrotech/ENDPOINTS?branch=develop) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)



**API_ENDPOINTS**

To create a set of API Endpoints that use data databases to store data in memory in place of data structures. These endpoints involve authentification with JWT



**GETTING STARTED**


The following are the API endpoints functions.

| ENDPOINT                                   | FUNCTIONALITY
|-------------------------------------------:|--------------------------------------------------:|
|POST/api/v2/auth/signup                     |Fetch all parcel delivery orders                   |      
|POST/api/v2/auth/login                      |Fetch a specific parcel delivery order             |
|PUT/api/v2/parcels/parcel_id                |Fetch all parcel delivery orders by a specific user|
|PUT/api/v2/parcels/parcelid/destination     |Cancel the specific parcel delivery order          |
|PUT/api/v2/parcels/parcel_id/location       |Create a parcel delivery order                     |


Users can Sign Up to their account. This is to allow users to create a new account. This an be tested with postman by passing the URL.

    [POST]: http://localhost:5000/api/v2/auth/signup


Users can login to their account and fetch all the deliery orders they make. This similarly can be tested with postman by passing the URL

    [POST]: http://localhost:5000/api/v2/auth/login


Users can get a speific order with provision of the order id and change the destination of that order. Test with postman.

    [PUT]: http://localhost:5000/api/v2/parcels/parcel_id/destination


Admin Users can can change the present location of pending orders by order id. The admin must be logged in as an admin first.

    [PUT]: http://localhost:5000/api/v2/parcels/parcel_id/location


Admin users can change the status of orders to either delivered upon delivery. The default status is InTransit.

    [PUT]: nhttp://localhost:5000/api/v2/parcels/parcel_id/status



**Requirement Softwares**


    Install pytest.

    Install flask-restful.

    Install coverage.

    Install coeralls.

    Install virtualenv.

    Install Postman

    Install nose

    Install dotenv

    Install postgresql

    Install psycopg2-binary

    Create a Procfile

    Create a .travis.yml file

    Install JWT extended


.

**Delevoloping Environment**


Before setting the environment clone the repository to a local machine.
Create a development environment called api_en1 with virtualenv .
Pip install virtualenv. Make a folder called Environments to hold the enironments i.e [virtualenv api_env1] should be in the Environments folder.Then activate the Environment and work from there. In the environment install flask, flask-restful, coveralls, coverage and pytest. Pip freeze > requirements.txt - to create a text file that hold the installations of that environment incase there is need to export them to another enironment.


**SETTING UP DATABASE CONNECTION**


After installing the postgres and psycopg2 use the database file in the models folder for the primary connection to the models.
All the other necesseties of the connection are documented and found in the repo


**TESTS**



Then install all the requirements int the environment.
After installing all the requirements create a dotenv file and add the following run the server on the file by typing

    export FLASK_DEBUG=true

    export FLASK_APP=run.py

    export DB_NAME="postgres"

    export DB_USER="postgres"

    export DB_HOST="localhost"

    export DB_PASSWORD="postgres"

    export SECRET_KEY="thisisarrotech"


Start Postman app. To test the endpoints use all the links provided above for each case.

Then the app is hosted on heroku as sendit-endpoints. The links from heroku are pasted on postman to create a onnection between the two.



Integrate GitHub with Travis CI to provide a continuous integration and an automated testing. Integrate GitHub with coveralls to provide test coverage of all tests.
Similarly the app is integrated with coveralls to test coverage and added a badge in the README file.
Finally integrated the app with code climate to check maintainability.



**Author**

     Harun Gachanja Gitundu

**Contributors to the project**

     Victor. Acting learning facilitator

     Brian mambo

     Mwangi.
