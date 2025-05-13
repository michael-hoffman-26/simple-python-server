from flask import Blueprint, jsonify, request, make_response
from repositories.factory import create_user_repository
from service.factory import create_user_service

users_bp = Blueprint('users', __name__)
user_repository = create_user_repository()
user_service = create_user_service(user_repository)

@users_bp.route('/')
def home():
    response = make_response(user_service.get_home())
    response.status_code = 200
    return response

@users_bp.route('/api/hello')
def hello():
    response = make_response(jsonify(user_service.get_hello()))
    response.status_code = 200
    return response

@users_bp.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    processed_data = user_service.process_echo_data(data)
    response = make_response(jsonify(processed_data))
    response.status_code = 201
    response.headers['Custom-Header'] = 'Some Value'
    return response

@users_bp.route('/api/greet/<name>')
def greet(name):
    greeting = user_service.create_greeting(name)
    response = make_response(jsonify(greeting), 200)
    # response.status_code = 200
    return response

# New user management endpoints
@users_bp.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = user_service.create_user(user_data)
    response = make_response(jsonify({'id': user_id, **user_data}), 201)
    return response

@users_bp.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        response = make_response(jsonify(user), 200)
    else:
        response = make_response(jsonify({'error': 'User not found'}), 404)
    return response

@users_bp.route('/api/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    response = make_response(jsonify(users), 200)
    return response

@users_bp.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    if user_service.update_user(user_id, user_data):
        response = make_response(jsonify({'id': user_id, **user_data}), 200)
    else:
        response = make_response(jsonify({'error': 'User not found'}), 404)
    return response

@users_bp.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.delete_user(user_id):
        response = make_response('', 204)
    else:
        response = make_response(jsonify({'error': 'User not found'}), 404)
    return response 