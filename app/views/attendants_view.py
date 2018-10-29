# product_views.py
from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.models.sale import Sale
from app.models.user import User
from app.views import create_store

bp = Blueprint('attendants_view', __name__, url_prefix='/api/v1/attendants')

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
def get_attendant():
    pass

""" Get details of a single attendant"""
@bp.route('/<attendant_id>', methods=['GET'])
def get_attendant_details():
    pass

""" Delete an attendant given the Id"""
@bp.route('<attendant_id>', methods=['DELETE'])
def delete_attendant(attendant_id):
    pass

""" Edit an attendant given the Id"""
@bp.route('<attendant_id>', methods=['PUT'])
def edit_attendant(attendant_id):
    pass
