from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib

def login(users):
    data = request.json
    username = data.get("username")
    password = data.get("password")
    password = hashlib.sha256(password.encode()).hexdigest()

    user = users.find_one({"username": username})

    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.get("password") != password:
        return jsonify({"message": "Incorrect Password"}), 400

    return jsonify({
        "message": "Successfully logged in",
        "token": None
    }), 200
