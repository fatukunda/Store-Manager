from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.controllers import auth_controller

bp = Blueprint('auth_view', __name__, url_prefix='/api/v1/auth')

""" AUTHENTICATION ROUTES"""

@bp.route('/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    if not username:
        return jsonify({"message": "Specify the Username"}), 400
    if not password:
        return jsonify({"message": "Specify the Password"}), 400
    user = auth_controller.login(username, password)
    # auth.pw_hash
    if not user:
        return jsonify({"message": "User not found"}), 404  
    access_token = ''
    if user['user_type'] == 'admin':
        access_token = create_access_token(identity='admin')
    else:
        access_token = create_access_token(identity= username)
        
    return jsonify(access_token=access_token), 200


    
