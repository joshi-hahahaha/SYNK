from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib
import re
import math
import datetime

def add_event(events):
    data = request.json

    # EXTRACT LOCATION INFORMATION
    id = data["id"]
    name = data["name"]
    description = data["description"]
    host = data["host"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    isPublic = data["isPublic"]
    startTime = data["startTime"]
    endTime = data["endTime"]

    # ERROR CHECKING MAYBE

    event_id = events.insert_one({
        "id" : id,
        "name" : name,
        "description" : description,
        "host" : host,
        "longitude" : longitude,
        "latitude" : latitude,
        "isPublic" : isPublic,
        "startTime" : startTime,
        "endTime" : endTime,
    })
    return jsonify({
                    "message" : "event registered",
                    "eventId" : event_id
                    }), 200

def nearby_events(events):
    data = request.json
    longitude = data["longitude"]
    latitude = data["latitude"]

    nearby = events.aggregate([
        {
            "$geoNear": {
                "near": { "type": "Point", "coordinates": [longitude, latitude] },
                "distanceField": "dist.calculated",  # Field to store the calculated distance
                "maxDistance": 5000,  # Maximum distance (in meters, 5km)
                "spherical": True  # Use spherical geometry (Haversine formula)
            }
        }
    ])

    # Nearby is a list of objects we can then return in json
    return jsonify({
                    "data": nearby
                    }), 200
