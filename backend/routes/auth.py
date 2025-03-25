from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib
import re
import jwt
import datetime

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

def register(users):
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    password = hashlib.sha256(password.encode()).hexdigest()

    invalid_character = re.compile(r"^.*[^a-zA-Z '-]")

    # username limitations
    if len(username) < 2 or len(username) > 20:
        return jsonify({"message": "Username is not of the appropriate character length"}), 400

    existing_username = users.find_one({"username": username})
    if existing_username:
        return jsonify({"message": "Username has been taken! Please enter a new username"}), 400


    # email limitations
    existing_email = users.find_one({"email": email})
    if existing_email:
        return jsonify({"message": "Email already exists! Please provide another email"}), 400

    user_id = users.insert_one({
        "username": username,
        "email": email,
        "password": password
    }).inserted_id

    token = jwt.encode({
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=3600)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({
        "message": "Successfully registered a profile",
        "token": token
    }), 201

def logout():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token is missing"}), 400

    token_blacklist.add(token)

    return jsonify({"message: Successfully logged out"}), 200

