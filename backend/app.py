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

print("DEBUG")
users = users_collection.find()
print("Users in the 'users' collection:")
for user in users:
    print(user)


#-----------------------------------------------------------------------------#
#-------------------------------- AUTH ROUTES --------------------------------#
#-----------------------------------------------------------------------------#
@app.route("/auth/login", methods=["GET"])
def login():
    return auth.login(users)

@app.route("/auth/register", methods=["POST"])
def register():
    return auth.register(users)

@app.route("/auth/logout", methods=["DELETE"])
def logout():
    return auth.logout()

@app.route("/events", methods=["POST"])
def post_event():
    return events.add_event(events)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
