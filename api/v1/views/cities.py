#!/usr/bin/python3
"""
    This Module contains the routes for the CRUD
    for the cities
"""
from api.v1.views import app_views
from models.city import City
from models.state import State
from models import storage
from flask import abort, jsonify, request


@app_views.route('/states/<state_id>/cities', strict_slashes=True, methods=['GET'])
def state_cities(state_id):
    """This Method Retrieves the list of all CIty Objects of a state"""
    state_obj = None
    cities = []
    for state in storage.all(State).values():
        if state.id == state_id:
            state_obj = state
    for city in state_obj.cities:
        cities.append(city.to_dict())
    if state:
        return jsonify(cities), 201
    abort(404)


@app_views.route('/cities/<city_id>', strict_slashes=True, methods=['GET'])
def get_cities(city_id):
    """This Method Retrieves a city from the database based on the id"""
    for city in storage.all(City).values():
        if city.id == city_id:
            return jsonify(city.to_dict()), 200
    abort(404)

@app_views.route('/cities/<city_id>', strict_slashes=True, methods=['DELETE'])
def delete_cities(city_id):
    """This Method Deletes a city object from the storage"""
    for city in storage.all(City).values():
        if city.id == city_id:
            storage.delete(city)
            storage.save()
            return jsonify({}), 200
    abort(404)


@app_views.route('/states/<state_id>/cities', strict_slashes=True, methods=['POST'])
def post_cities(state_id):
    """This Method creates a City"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in data.keys():
        return jsonify({"error": "Missing name"}), 400
    for state in storage.all(State).values():
        if state.id == state_id:
            obj = City(state_id=state_id, **data)
            storage.new(obj)
            storage.save()
            return jsonify(obj.to_dict()), 201

    abort(404)


@app_views.route('/cities/<city_id>', strict_slashes=True, methods=['PUT'])
def put_city(city_id):
    """This Method updates the data of a city"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for city_obj in storage.all("City").values():
        if city_id == city_obj.id:
            city = city_obj.to_dict()
            storage.delete(city_obj)
            for key in data.keys():
                if key not in ["id", "updated_at"]:
                    city[key] = data[key]
            city_obj = City(**city)
            storage.new(city_obj)
            city_obj.save()
            return jsonify(city), 200
    abort(404   )