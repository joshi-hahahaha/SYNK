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

def nearby_events(events, latitude, longitude):
    for e in events.find():
        lat = e['latitude']
        lng = e['longitude']
        events.update_one(
            {"_id": e["_id"]},
            {"$set": {"location": {"type": "Point", "coordinates": [lng, lat]}}}
        )

    # Find nearby events
    nearby = events.find({
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                },
                "$maxDistance": 60000  # Max distance in meters
            }
        }
    })

    # Prepare the result and remove the _id field
    ret = []
    for e in nearby:
        e.pop('_id')  # Remove the _id field
        ret.append(e)

    # Return the results as a JSON response
    return jsonify(ret)
