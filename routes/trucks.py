from flask import Blueprint, jsonify, request, make_response
from service.factory import get_warehouse_service

trucks_bp = Blueprint('trucks', __name__)
truck_service = get_warehouse_service()

# New user management endpoints
@trucks_bp.route('/api/trucks', methods=['POST'])
def create_truck():
    truck_data = request.get_json()
    truck_id = truck_service.create_truck(truck_data)
    response = make_response(jsonify({'id': truck_id, **truck_data}), 201)
    return response

@trucks_bp.route('/api/trucks/<int:truck_id>', methods=['GET'])
def get_truck(truck_id):
    truck = truck_service.get_truck(truck_id)
    if truck:
        response = make_response(jsonify(truck), 200)
    else:
        response = make_response(jsonify({'error': 'Truck not found'}), 404)
    return response

@trucks_bp.route('/api/trucks', methods=['GET'])
def get_all_trucks():
    # TODO: We should support pagination here to handle large datasets efficiently
    trucks = truck_service.get_all_trucks()
    response = make_response(jsonify(trucks), 200)
    return response

@trucks_bp.route('/api/trucks/<int:truck_id>', methods=['PUT'])
def update_truck(truck_id):
    truck_data = request.get_json()
    if truck_service.update_truck(truck_id, truck_data):
        response = make_response(jsonify({'id': truck_id, **truck_data}), 200)
    else:
        response = make_response(jsonify({'error': 'Truck not found'}), 404)
    return response

@trucks_bp.route('/api/trucks/<int:truck_id>', methods=['DELETE'])
def delete_truck(truck_id):
    if truck_service.delete_truck(truck_id):
        response = make_response(f'DELETED TRUCK ID: {truck_id}', 204)
    else:
        response = make_response(jsonify({'error': 'Truck not found'}), 404)
    return response 