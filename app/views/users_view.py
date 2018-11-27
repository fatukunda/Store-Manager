# User_views.py
from flask import Blueprint, request, jsonify
from app.models.user import User
from app.controllers import user_controller
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import search_sales_person
from flask_cors import CORS

bp = Blueprint('users_view', __name__, url_prefix='/api/v1/attendants')
CORS(bp)

""" ATTENDANT ROUTES"""


@bp.route('', methods=['POST'])
@jwt_required
def register_attendant():
    """ Register an attendant"""
    current_user = get_jwt_identity()
    current_user_role = search_sales_person(current_user)
    if current_user_role['user_type'] == 'admin':
        request_data = request.get_json()
        first_name = request_data['first_name']
        last_name = request_data['last_name']
        email = request_data['email']
        username = request_data['username']
        password = request_data['password']
        user_controller.create_user(first_name, last_name, username, email, password)
        return jsonify('User %s created successfully' % first_name), 201
    else:
        return jsonify({"message": "Not authorized to access this page"}), 401


@bp.route('/', methods=['GET'])
@jwt_required
def get_attendants():
    """ Get a list of attendants in the store"""
    current_user = get_jwt_identity()
    user_role = search_sales_person(current_user)
    if user_role['user_type'] == 'admin':
       return jsonify(user_controller.get_all_users())
    else:
       return jsonify({"message": "Not allowed to access this page"}), 401
    
@bp.route('/<attendant_id>', methods=['GET'])
@jwt_required
def get_attendant_details(attendant_id):
    """ Get details of a single attendant"""
    current_user = get_jwt_identity()
    user_role = search_sales_person(current_user)
    if user_role['user_type'] == 'admin' or user_role['user_id'] == current_user:
        user = user_controller.get_user_details(attendant_id)
        if user:
            return jsonify(user_controller.get_user_details(attendant_id)), 200
        else:
            return jsonify({"message": "No such user was found"}), 404
    else:
        return jsonify({"message" : "Not allowed to access this page"}), 401

@bp.route('/<attendant_id>', methods=['PUT'])
@jwt_required
def make_attendant_admin(attendant_id):
    """ Give administrator rights"""
    current_user = get_jwt_identity()
    user_role = search_sales_person(current_user)
    if user_role['user_type'] == 'admin':
        if not request.is_json:
            return jsonify({"message": "Missing JSON in request"}), 400
        role = request.json.get('role')
        if not role:
            return jsonify({"message": "Missing role parameter"}), 400
        user = user_controller.give_admin_rights(attendant_id, role)
        if user:
            return jsonify({"message": "Admin rights successfully assigned to user"})
    else:
        return jsonify({"message": "Not allowed to access this page"})

@bp.route('<attendant_id>', methods=['DELETE'])
@jwt_required
def delete_attendant(attendant_id):
    """ Delete an attendant given the Id"""
    current_user = get_jwt_identity()
    user_role = search_sales_person(current_user)
    if user_role['user_type'] == 'admin':
        rows_deleted = user_controller.delete_attendant(attendant_id)
        if not rows_deleted:
            return  jsonify({"message": "Unable to find user"})
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "Not authorized to access this page"})
