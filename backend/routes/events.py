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
    # nearby = events.aggregate([
    #     {
    #         "$geoNear": {
    #             "near": {"type": "Point", "coordinates": [longitude, latitude]},
    #             "distanceField": "dist.calculated",
    #             "maxDistance": 5000,  # Specify max distance here
    #             "spherical": True
    #         }
    #     }
    # ])

    ret = []
    for e in events.find():
        e.pop('_id')
        ret.append(e)

    return jsonify(ret)
