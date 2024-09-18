#!/usr/bin/python3
"""
    This Module contains all the Amenities Routes
"""
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from flask import abort, jsonify, request

@app_views.route('/amenities/<amenity_id>', strict_slashes=True, mmethods=['GET'])
def get_amenities(amenity_id = None):
    """
        This Method returns all the Amenities

        Arguments:
            amenity_id: the amenity Id to be returned or None.

        Return:
            this method returns the amenity value to be returned or All if the amenit_id is None.
    """
    amenities = []
    if amenity_id == None:
        for amenity in storage.all(Amenity).values():
            amenities.append(amenity.to_dict())
        return jsonify(amenities), 200
    else:
        amenity = storage.get(Amenity, amenity_id)
        if not amenity:
            abort(404)

@app_views.route('/amenities/<amenity_id>', strict_slashes=True, methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
