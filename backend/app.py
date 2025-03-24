import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from backend.routes.login import login as l
from backend.helpers import generate_secret_key

#-----------------------------------------------------------------------------#
#-------------------------------- APP SET UP ---------------------------------#
#-----------------------------------------------------------------------------#
# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
generate_secret_key()
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

db = client["synk-db"]

users = db["users"]
events = db["events"]

#-----------------------------------------------------------------------------#
#-------------------------------- AUTH ROUTES --------------------------------#
#-----------------------------------------------------------------------------#
@app.route("/auth/login", methods=["GET"])
def login():
    return l(users)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
