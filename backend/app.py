import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from routes import auth, events

#-----------------------------------------------------------------------------#
#-------------------------------- APP SET UP ---------------------------------#
#-----------------------------------------------------------------------------#
# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["synk-db"]

users_collection = db["users"]
events_collection = db["events"]
events_collection.create_index([("location", "2dsphere")])

#-----------------------------------------------------------------------------#
#-------------------------------- AUTH ROUTES --------------------------------#
#-----------------------------------------------------------------------------#
@app.route("/auth/login", methods=["GET"])
def login():
    return auth.login(users_collection)

@app.route("/auth/register", methods=["POST"])
def register():
    return auth.register(users_collection)

@app.route("/events", methods=["POST"])
def post_event():
    return events.add_event(events_collection)

@app.route("/events", methods=["GET"])
def get_events():
    return events.nearby_events(events_collection)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
