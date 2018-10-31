# User_views.py

from flask import Blueprint, request, jsonify
from app.models.user import User
from app.controllers import user_controller

bp = Blueprint('users_view', __name__, url_prefix='/api/v1/attendants')

""" ATTENDANT ROUTES"""

""" Register an attendant"""
@bp.route('', methods=['POST'])
def register_attendant():
    request_data = request.get_json()
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    email = request_data['email']
    username = request_data['username']
    password = request_data['password']
    role = request_data['role']
    user_controller.create_user(first_name, last_name, username, email, password, role)
    return jsonify('User %s created successfully' % first_name), 201

""" Get a list of attendants in the store"""
@bp.route('/', methods=['GET'])
def get_attendants():
   return jsonify(user_controller.get_all_users())

""" Get details of a single attendant"""
@bp.route('/<attendant_id>', methods=['GET'])
def get_attendant_details(attendant_id):
    user = user_controller.get_user_details(attendant_id)
    if user:
        return jsonify(user_controller.get_user_details(attendant_id)), 200
    else:
        return jsonify({"message": "No such user was found"}), 404

@bp.route('/<attendant_id>', methods=['PUT'])
def make_attendant_admin(attendant_id):
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    role = request.json.get('role')
    if not role:
        return jsonify({"message": "Missing role parameter"}), 400
    user = user_controller.give_admin_rights(attendant_id, role)
    if user:
        return 'Admin rights successfully assigned to user'

""" Delete an attendant given the Id"""
@bp.route('<attendant_id>', methods=['DELETE'])
def delete_attendant(attendant_id):
    rows_deleted = user_controller.delete_attendant(attendant_id)
    if rows_deleted:
        return 'User deleted successfully'

""" Edit an attendant given the Id"""
@bp.route('<attendant_id>', methods=['PUT'])
def edit_attendant(attendant_id):
    pass
