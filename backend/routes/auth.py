from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib
import re
import jwt
import datetime

from helpers import hash_password

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


def register(db):
    data = request.json
    if not data:
        return jsonify({"error": "no data provided"}), 400

    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "missing required fields"}), 400

    existing_user = db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "user is already registered"}), 400

    user_document = {
        "name": username,
        "email": email,
        "hashed_password": hash_password(password),
    }

    result = db.users.insert_one(user_document)

    return jsonify({
        "user_id": str(result.inserted_id),
        "message": "user registered successfully"
    }), 201


def logout():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token is missing"}), 400

    token_blacklist.add(token)

    return jsonify({"message: Successfully logged out"}), 200

