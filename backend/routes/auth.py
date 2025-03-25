from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib
import re
import jwt
import datetime

from helpers import create_token, hash_password, verify_password, verify_token

def login(db, secret_key):
    data = request.json
    
    if not data:
        return jsonify({"error": "no data provided"}), 400
    
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "missing required fields"}), 400
    
    valid_user = db.users.find_one({"email": email})
    
    if not valid_user:
        return jsonify({"error": "invalid email or password"}), 401

    valid_password = verify_password(password, valid_user.get("hashed_password"))
    if not valid_password:
        return jsonify({"error": "invalid email or password"}), 401

    is_confirmed = valid_user.get("is_confirmed")
    if not is_confirmed:
        return jsonify({"error": "account has not yet been confirmed"}), 403

    token = create_token(str(valid_user.get("_id")), secret_key)

    return jsonify({
        "user_id": str(valid_user.get('_id')),
        "token": token,
        "message": "user login successful",
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

def logout(secret_key, blacklist):
    # Extract token from Authorization Header
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({"error": "token is missing"}), 401

    # check if valid is invalid
    if verify_token(token, secret_key) is None:
        return jsonify({"error": "invalid token"}), 401

    # check if token is blacklisted
    if blacklist.find_one({"token": token}) is not None:
        return jsonify({"error": "invalid token"}), 401

    blacklist.insert_one({"token": token})
    return jsonify({"message": "Logged out successfully"}), 200 