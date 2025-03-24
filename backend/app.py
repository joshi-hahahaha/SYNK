from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from backend.routes.login import login as l

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")
client = MongoClient(MONGO_URI)
db = client.get_database()

users = db["users"]
events = db["events"]

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/auth/login", methods=["GET"])
def login():
    return l(users)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
