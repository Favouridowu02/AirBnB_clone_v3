#!/usr/bin/python3
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from flask import abort, jsonify, request