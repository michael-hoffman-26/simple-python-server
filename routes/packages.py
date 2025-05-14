from flask import Blueprint, request, jsonify
from datetime import datetime
from service.factory import get_warehouse_service

# Initialize the blueprint
package_bp = Blueprint('packages', __name__)
warehouse_service = get_warehouse_service()

@package_bp.route('/packages', methods=['POST'])
def create_package():
    """Create a new package"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['length', 'width', 'height']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
            if not isinstance(data[field], (int, float)) or data[field] <= 0:
                return jsonify({'error': f'{field} must be a positive number'}), 400

        # Optional truck_id
        truck_id = data.get('truck_id')
        if truck_id is not None and not isinstance(truck_id, int):
            return jsonify({'error': 'truck_id must be an integer'}), 400

        # Create the package
        package_id = warehouse_service.create_package(
            length=data['length'],
            width=data['width'],
            height=data['height'],
            truck_id=truck_id
        )

        return jsonify({
            'message': 'Package created successfully',
            'package_id': package_id
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/packages', methods=['GET'])
def get_all_packages():
    """Get all packages"""
    try:
        packages = warehouse_service.get_all_packages()
        return jsonify(packages), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    """Get a specific package by ID"""
    try:
        package = warehouse_service.get_package(package_id)
        if package is None:
            return jsonify({'error': 'Package not found'}), 404
        return jsonify(package), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    """Update a package"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Validate numeric fields if provided
        for field in ['length', 'width', 'height']:
            if field in data and (not isinstance(data[field], (int, float)) or data[field] <= 0):
                return jsonify({'error': f'{field} must be a positive number'}), 400

        # Validate truck_id if provided
        if 'truck_id' in data and data['truck_id'] is not None and not isinstance(data['truck_id'], int):
            return jsonify({'error': 'truck_id must be an integer'}), 400

        # Check if package exists
        if not warehouse_service.get_package(package_id):
            return jsonify({'error': 'Package not found'}), 404

        # Update the package
        if warehouse_service.update_package(package_id, data):
            return jsonify({'message': 'Package updated successfully'}), 200
        return jsonify({'error': 'Failed to update package'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    """Delete a package"""
    try:
        if warehouse_service.delete_package(package_id):
            return jsonify({'message': 'Package deleted successfully'}), 200
        return jsonify({'error': 'Package not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/trucks/<int:truck_id>/packages', methods=['GET'])
def get_packages_by_truck(truck_id):
    """Get all packages assigned to a specific truck"""
    try:
        packages = warehouse_service.get_packages_by_truck(truck_id)
        return jsonify(packages), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
