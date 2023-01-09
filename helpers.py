import requests

from flask import redirect, render_template, request
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:test@cluster0.e6xf1kc.mongodb.net/?retryWrites=true&w=majority')

def get_count(city, state):
    """Count the UFO sightings for that city and state"""

    city_count = client['ufos']['ufos'].aggregate([
        {
            '$match': {
                'city':  city
            }
        }, {
            '$match': {
                'state': state
            }
        }, {
            '$count': 'ufo_count'
        }
    ])

    return city_count

def get_ufos(city, state):
    """Gets report of UFO sightings for that city and state"""

    recent_ufos = client['ufos']['ufos'].aggregate([
        {
            '$match': {
                'city': city
            }
        }, {
            '$match': {
                'state': state
            }
        }, {
            '$sort': {
                'datetime': -1
            }
        },
    ])

    return recent_ufos
