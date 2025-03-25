from flask import jsonify, request

from helpers import check_register_data, create_token, hash_password, verify_password

def login(db, secret_key: str):
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


    token = create_token(str(valid_user.get("_id")), secret_key)
    return jsonify({
        "userId": str(valid_user.get('_id')),
        "token": token,
        "message": "user login successful",
    }), 200


def register(db, secret_key: str):
    data = request.json
    if not data:
        return jsonify({"error": "no data provided"}), 400

    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    
    err = check_register_data(db, email, username, password)
    if err:
        return err

    existing_user = db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "user is already registered"}), 400

    user_document = {
        "name": username,
        "email": email,
        "hashed_password": hash_password(password),
    }

    # Insert into db
    result = db.users.insert_one(user_document)
    
    # Immediately take user from db for generated ObjectId
    user = db.users.find_one({"email": email})
    
    # AUTOMATICALLY LOG USER IN
    token = create_token(str(user.get("_id")), secret_key)

    return jsonify({
        "userId": str(result.inserted_id),
        "token": token,
        "message": "user registered successfully"
    }), 201

def logout(db):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization header missing or invalid"}), 401
    
    token = auth_header.split(" ")[1].strip()
    if not token:
        return jsonify({"error": "Token is empty"}), 401

    # Debug: Print token and collection status
    print(f"Token received: {token}")
    print(f"Blacklist count before check: {db.blacklist.count_documents({})}")
    print(f"Existing tokens: {list(db.blacklist.find({}, {'token': 1}))}")

    # Check blacklist - modified to be more precise
    existing = db.blacklist.find_one({"token": token})
    if existing:
        return jsonify({"error": "Token already invalidated"}), 401

    db.blacklist.insert_one({"token": token})

    return jsonify({"message": "Logged out successfully"}), 200