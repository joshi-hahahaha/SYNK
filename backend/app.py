import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from routes.login import login as l

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
    return l(users)

@app.route("/auth/register", methods=["POST"])
def register():
    return register(users)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
