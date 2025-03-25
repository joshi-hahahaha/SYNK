from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib

####### Incorrect ########

def user_update(users, db):  
    data = request.json
    username = data.get("username")
    if not data:
        return jsonify({"message": "Data is not provided"}), 400
    
    user = users.find_one({"username": username})

    
    update_user_details = {}
    if "firstName" in data:
        update_user_details["firstName"] = data["firstName"]

    if "lastName" in data:
        update_user_details["lastName"] = data["lastName"]

    if "username" in data:
        update_user_details["username"] = data["username"]
    
    if "email" in data:
        update_user_details["email"] = data["email"]
    
    if "password" in data:
        password = hashlib.sha256(data["password"].encode()).hexdigest()
        update_user_details["password"] = data["password"]

    if not update_user_details:
        return jsonify({"message": "No valid fields for updating"}), 400

    users_collection = db["users"]
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_user_details}
    )

    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404

    updated_user = users_collection.find_one({"_id": ObjectId(user_id)})


    return jsonify({
        "message": "Successfully updated a user profile",
        "user": {
            "id": str(updated_user["_id"]),
            "firstName": updated_user.get("firstName"),
            "lastName": updated_user.get("lastName"),
            "username": updated_user.get("username"),
            "password": updated_user.get("password"),
            "email": updated_user.get("email")
        }
    }), 200


def user_details(user_id, db):
    users_collection = db["users"]
    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_details = {
        "id": str(user["_id"]),
        "firstName": user.get("firstName"),
        "lastName": user.get("lastName"),
        "username": user.get("username"),
        "email": user.get("email"),
        "password": user.get("password")
    }

    return jsonify({"user": user_details}), 200
