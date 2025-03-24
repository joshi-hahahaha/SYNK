from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import hashlib
import re
import jwt
import datetime

def add_event(events):
    data = request.json

    # EXTRACT LOCATION INFORMATION
    # EXTRACT TIME INFORMATION
    # WHATEVER OTHER INFROMAT

    # ERROR CHECKING MAYBE

    # event_id = events.insert_one({
    #     .
    #     .
    #     .
    #     .
    #     .
    # })
    return jsonify({"message" : "event registered" }), 200

def nearby_events(events):
    # This is going to be very inefficient
    # Linear search of every event
    data = request.json

    # extract all events
    # calculate distance to user
    # if under threshold radius add to a list
    # send the list back

    return