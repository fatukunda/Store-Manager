# User_views.py
from flask import Blueprint, request, jsonify
from app.models.user import User
from app.controllers import user_controller
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('users_view', __name__, url_prefix='/api/v1/attendants')

""" ATTENDANT ROUTES"""


@bp.route('', methods=['POST'])
@jwt_required
def register_attendant():
    """ Register an attendant"""
    current_user = get_jwt_identity()
    if current_user == 'admin':
        request_data = request.get_json()
        first_name = request_data['first_name']
        last_name = request_data['last_name']
        email = request_data['email']
        username = request_data['username']
        password = request_data['password']
        role = request_data['role']
        user_controller.create_user(first_name, last_name, username, email, password, role)
        return jsonify('User %s created successfully' % first_name), 201
    else:
        return jsonify({"message": "Not authorized to access this page"}), 401


@bp.route('/', methods=['GET'])
@jwt_required
def get_attendants():
    """ Get a list of attendants in the store"""
    current_user = get_jwt_identity()
    if current_user == 'admin':
        return jsonify(user_controller.get_all_users())
    else:
        jsonify({"message": "Not allowed to access this page"}), 401

@bp.route('/<attendant_id>', methods=['GET'])
@jwt_required
def get_attendant_details(attendant_id):
    """ Get details of a single attendant"""
    current_user = get_jwt_identity()
    if current_user:
        user = user_controller.get_user_details(attendant_id)
        if user:
            return jsonify(user_controller.get_user_details(attendant_id)), 200
        else:
            return jsonify({"message": "No such user was found"}), 404
    else:
        return jsonify({"message": "Not authorized to access this page"})

@bp.route('/<attendant_id>', methods=['PUT'])
@jwt_required
def make_attendant_admin(attendant_id):
    """ Give administrator rights"""
    current_user = get_jwt_identity()
    if current_user == 'admin':
        if not request.is_json:
            return jsonify({"message": "Missing JSON in request"}), 400
        role = request.json.get('role')
        if not role:
            return jsonify({"message": "Missing role parameter"}), 400
        user = user_controller.give_admin_rights(attendant_id, role)
        if user:
            return 'Admin rights successfully assigned to user'
    else:
        return jsonify({"message": "Not allowed to access this page"})

@bp.route('<attendant_id>', methods=['DELETE'])
@jwt_required
def delete_attendant(attendant_id):
    """ Delete an attendant given the Id"""
    current_user =get_jwt_identity()
    if current_user == 'admin':
        rows_deleted = user_controller.delete_attendant(attendant_id)
        if rows_deleted:
            return 'User deleted successfully'
    else:
        return jsonify({"message": "Not authorized to access this page"})

""" Edit an attendant given the Id"""
@bp.route('<attendant_id>', methods=['PUT'])
def edit_attendant(attendant_id):
    pass
