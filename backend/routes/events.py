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
    # This is going to be very inefficient
    # Linear search of every event
    data = request.json
    longitude = data["longitude"]
    latitude = data["latitude"]

    # Haversine formula

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


def haversine(lat1, lon1, lat2, lon2):
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c
