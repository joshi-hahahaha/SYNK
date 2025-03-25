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
        "role": valid_user.get("role"),
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
    
    # password = hashlib.sha256(password.encode()).hexdigest()

    # invalid_character = re.compile(r"^.*[^a-zA-Z '-]")

    # # Required fields are missing
    # if not firstName or not lastName or not username or not password or not reconfirmPassword:
    #     return jsonify({"message": "All fields are required"}), 400


    # # firstName limitations
    # if len(firstName) < 2 or len(firstName) > 20:
    #    return jsonify({"message": "First name is not of the appropriate character length"}), 400

    # match = invalid_character.match(firstName)
    # if not match:
    #     return jsonify({"message": "First name uses inappropriate characters"}), 400


    # # lastName limitations
    # if len(lastName) < 2 or len(lastName) > 20:
    #     return jsonify({"message": "Last name is not of the appropriate character length"}), 400

    # match = invalid_character.match(lastName)
    # if not match:
    #     return jsonify({"message": "Last name uses inappropriate characters"}), 400


    # # username limitations
    # if len(username) < 2 or len(username) > 20:
    #     return jsonify({"message": "Username is not of the appropriate character length"}), 400

    # existing_username = users.find_one({"username": username})
    # if existing_username:
    #     return jsonify({"message": "Username has been taken! Please enter a new username"}), 409


    # # email limitations
    # existing_email = users.find_one({"email": email})
    # if existing_email:
    #     return jsonify({"message": "Email already exists! Please provide another email"}), 409


    # # password limitations
    # if password != reconfirmPassword:
    #     return jsonify({"message": "Passwords does not match up! Please retype your password"}), 400

    # user_id = users.insert_one({
    #     "firstName": firstName,
    #     "lastName": lastName,
    #     "username": username,
    #     "email": email,
    #     "password": password
    # }).inserted_id

    # token = jwt.encode({
    #     "user_id": user_id,
    #     "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=3600)
    # }, app.config['SECRET_KEY'], algorithm="HS256")

    # return jsonify({
    #     "message": "Successfully registered a profile",
    #     "token": token
    # }), 201


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

