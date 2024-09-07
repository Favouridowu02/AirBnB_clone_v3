#!/usr/bin/python3
"""
    This Module contains the index
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status of the application"""
    return jsonify({"status": "OK"})
