#!/usr/bin/python3
"""
    This Module contains the v1 of the api

    Content:
        app_views = A Blueprint with prefix /api/v1
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *

print("\n\n",app_views)

