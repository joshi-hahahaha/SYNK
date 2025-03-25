import os
import re
import secrets
import bcrypt
import datetime

from flask import jsonify
import jwt

# Hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
  
  # Verify password
def verify_password(provided_password, hashed_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), hashed_password)

# create JWT token
def create_token(user_id, secret_key, time_to_expire=3600):
    expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=time_to_expire) # expires after 1 day (can change)

    payload = {
        "user_id": user_id,
        "exp": expiration_time
    }

    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token

# generating secret key to be used to create and verify tokens 
def generate_secret_key():
    secret_key = secrets.token_hex(32)

    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(f'\nSECRET_KEY={secret_key}\n')
    else:
        with open('.env', 'a') as f:
            if 'SECRET_KEY' not in open('.env').read():
                f.write(f'\nSECRET_KEY={secret_key}\n')
                
def verify_token(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None # token has expired
    except jwt.InvalidTokenError:
        return None # invalid token

# check register data
def check_register_data(db, email, username, password):
    invalid_character = re.compile(r"^.*[a-zA-Z0-9]")

    if not username or not password:
        return jsonify({"message": "All fields are required"}), 400

    match = invalid_character.match(username)
    if not match:
        return jsonify({"message": "username uses inappropriate characters"}), 400

    existing_email = db.users.find_one({"email": email})
    if existing_email:
        return jsonify({"message": "Email already exists! Please provide another email"}), 400
