"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint 
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__) # Flask provides the Blueprint class as a way to organize and structure a larger application by grouping related views, templates, etc. 
                                 # It's a built-in feature of Flask, so we just need to import it to use it. 
# The line creates a Blueprint named 'api' with 2 arguments: The first one is the name of the Blueprint (api), and the second one (__name__) is used to determine where the Blueprint is defined.
# In your main app file (app.py), we register the blueprint

# Allow CORS requests to this API
CORS(api)

# example route
@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {"message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"}
    return jsonify(response_body), 200

# este es mi login donde hay un username y tiene que ser = a "test" y password que es = a "test". Esto es lo que tenemos que enviar en Postman para logearse
# Note: In the browser, a POST cannot be seen, only a GET. To view the POST, we have to use tools like Postman (first, make it public;if not it will give me a 401 error), or via fetch in Reach 
# In Postman it will give me as result the token
@api.route("/login", methods=["POST"])   #we change app for api as we are using Blueprint. 
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # here we set the logic to consult if user exists in our DB
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401  # jsonify transforms our python code into JSON so our front can receive it. We can receive 2 parameters in our return, so we also receive the success code 200 (ok)
    
    # create_access_token() function is used to actually generate the JWT.
    access_token = create_access_token(identity=[username, True])  # Note: if I want to send more info than the username in the payload/identity, I create a list:(identity=[username, True, "other info"]). If not: (identity=username)
    return jsonify(access_token=access_token)  # remember to import create_access_token!

#PRIVATE/PROTECTED ROUTE:
# We define a route which is protected and can only be accessed by clients providing a valid JWT in the request headers
@api.route("/private", methods=["GET"]) #change app for api!
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity() # Retrieve the identity of the current user from the JWT payload (the variable current_user will save what we have set inside the token as the identity, in our case, the username:  access_token = create_access_token(identity=username))
    return jsonify(logged_in_as=current_user), 200 # and it will return a json response indicating the logged-in user


# Profile route so the user can enter its profile:
@api.route("/profile", methods=["GET"]) #change app for api!
@jwt_required() # it's the user's personal profile, so I protect it using the decorator @jwt_required()
def profile():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    if current_user[1]:  # we will get the identity, which we made it a list (identity=[username, True]), so to access the list to check if the current_user is True we select the i=1. And if true, it will print in the console "Value is True". 
        print("Value is True")
    response_body = {}
    response_body["logged_in_as"] = current_user   # this is our response_body["result"]
    response_body["message"] = "show user profile"
    return response_body, 200
