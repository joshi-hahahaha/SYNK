import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from helpers import generate_secret_key
from routes import auth, user, events

#-----------------------------------------------------------------------------#
#-------------------------------- APP SET UP ---------------------------------#
#-----------------------------------------------------------------------------#
# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, origins=["https://synk-seven.vercel.app", "http://localhost:3000"])

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

generate_secret_key()
load_dotenv()

db = client["synk-db"]

users_collection = db["users"]
events_collection = db["events"]
blacklist = db["blacklist"]

events_collection.create_index([("location", "2dsphere")])

SECRET_KEY = os.getenv('SECRET_KEY')

#-----------------------------------------------------------------------------#
#-------------------------------- AUTH ROUTES --------------------------------#
#-----------------------------------------------------------------------------#
@app.route("/auth/login", methods=["POST"])
def login():
    return auth.login(db, SECRET_KEY)

@app.route("/auth/register", methods=["POST"])
def register():
    return auth.register(db, SECRET_KEY)

@app.route("/auth/logout", methods=["DELETE"])
def logout():
    return auth.logout(db)

@app.route("/user/update", methods=["PUT"])
def user_update():
    return user.user_update(users_collection, db)

@app.route("/user/details", methods=["GET"])
def user_details():
    return user.user_details(users_collection, db)

@app.route("/events", methods=["POST"])
def post_event():
    return events.add_event(events_collection)

@app.route("/events", methods=["GET"])
def get_events():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    return events.nearby_events(events_collection, latitude, longitude)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
