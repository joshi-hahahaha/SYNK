from flask import Flask, jsonify, request
import re
from email_validator import validate_email, EmailNotValidError
import hashlib
import jwt
import datetime


def register(users):
    data = request.json
    firstName = data.get("firstName")
    lastName = data.get("lastName")
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    reconfirmPassword = data.get("reconfirmPassord")
    
    password = hashlib.sha256(password.encode()).hexdigest()


    invalid_character = re.compile(r"^.*[^a-zA-Z '-]")

    # Required fields are missing
    if not firstName or not lastName or not username or not password or not reconfirmPassword:
        return jsonify({"message": "All fields are required"}), 400
    

    # firstName limitations
    if len(firstName) < 2 or len(firstName) > 20:
       return jsonify({"message": "First name is not of the appropriate character length"}), 400

    match = invalid_character.match(firstName)
    if not match:
        return jsonify({"message": "First name uses inappropriate characters"}), 400
 

    # lastName limitations
    if len(lastName) < 2 or len(lastName) > 20:
        return jsonify({"message": "Last name is not of the appropriate character length"}), 400

    match = invalid_character.match(lastName)
    if not match:
        return jsonify({"message": "Last name uses inappropriate characters"}), 400


    # username limitations
    if len(username) < 2 or len(username) > 20:
        return jsonify({"message": "Username is not of the appropriate character length"}), 400

    existing_username = users.find_one({"username": username})
    if existing_username:
        return jsonify({"message": "Username has been taken! Please enter a new username"}), 409

    # email limitations
    valid_email = validate_email(email)
    if not valid_email:
        return jsonify({"message": "Invalid email inputted"}), 400
    
    existing_email = users.find_one({"email": email})
    if existing_email:
        return jsonify({"message": "Email already exists! Please provide another email"}), 409
 

    # password limitations
    if password != reconfirmPassword:
        return jsonify({"message": "Passwords does not match up! Please retype your password"}), 400

    
    user_id = users.insert_one({
        "firstName": firstName,
        "lastName": lastName,
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
