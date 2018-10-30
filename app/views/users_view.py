# User_views.py

from flask import Blueprint, request, jsonify
from app.models.user import User

bp = Blueprint('users_view', __name__, url_prefix='/api/v1/attendants')

""" ATTENDANT ROUTES"""

""" Register an attendant"""
@bp.route('', methods=['POST'])
def register_attendant():
    attendant = User()
    request_data = request.get_json()
    attendant.first_name = request_data['first_name']
    attendant.last_name = request_data['last_name']
    attendant.email = request_data['email']
    attendant.username = request_data['username']
    attendant.set_password = request_data['password']
    attendant.role = request_data['role']
    attendant.create_user()
    return jsonify('User %s created successfully' % attendant.first_name), 201

""" Get a list of attendants in the store"""
@bp.route('/', methods=['GET'])
def get_attendants():
   return jsonify(User.get_all_users())

""" Get details of a single attendant"""
@bp.route('/<attendant_id>', methods=['GET'])
def get_attendant_details(attendant_id):
    user = User.get_user_details(attendant_id)
    if user:
        return jsonify(User.get_user_details(attendant_id)), 200
    else:
        return jsonify({"message": "No such user was found"}), 404

@bp.route('/<attendant_id>', methods=['PUT'])
def make_attendant_admin(attendant_id):
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    role = request.json.get('role')
    if not role:
        return jsonify({"message": "Missing role parameter"}), 400
    user = User.give_admin_rights(attendant_id, role)
    if user:
        return 'Admin rights successfully assigned to user'

""" Delete an attendant given the Id"""
@bp.route('<attendant_id>', methods=['DELETE'])
def delete_attendant(attendant_id):
    rows_deleted = User.delete_attendant(attendant_id)
    if rows_deleted:
        return 'User deleted successfully'

""" Edit an attendant given the Id"""
@bp.route('<attendant_id>', methods=['PUT'])
def edit_attendant(attendant_id):
    pass
