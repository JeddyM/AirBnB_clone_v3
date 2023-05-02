#!/usr/bin/python3
"""Module to route status"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage

classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
    }


@app_views.route('/status')
def status():
    """Returns a JSON: "status": "OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Endpoint that retrieves the number of each objects by type"""
    dictionary = {}
    dictionary = {key: storage.count(value) for key, value in classes.items()}
    return jsonify(dictionary)


if __name__ == "__main__":
    pass
