from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.auth import Auth
from app.controllers import auth_controller
from datetime import timedelta

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
    auth = Auth(username, password)
    # auth.pw_hash
    user = auth_controller.login(auth.username, auth.password)
    if not user:
        return jsonify({"message": "User not found"}), 404  
    access_token = ''
    user_id = user['user_id']
    access_token = create_access_token(identity= user_id, expires_delta= timedelta(hours=2))
    return jsonify(access_token=access_token), 200


    
