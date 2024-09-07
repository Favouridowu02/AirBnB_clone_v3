#!/usr/bin/python3
"""
    This Module contains the index
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

count = {
    "amenities": storage.count(Amenity) or 0,
    "cities": storage.count(City) or 0,
    "places": storage.count(Place) or 0,
    "reviews": storage.count(Review) or 0,
    "states": storage.count(State) or 0,
    "users": storage.count(User) or 0
}


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status of the application"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """An EndPoint that retrieves the number of each objects by type"""
    return jsonify(count)
