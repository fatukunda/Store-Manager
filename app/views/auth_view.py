from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.auth import Auth

bp = Blueprint('auth_view', __name__, url_prefix='/api/v1/auth')

""" AUTHENTICATION ROUTES"""

@bp.route('/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
    auth = Auth(username, password)
    user = auth.login()
    if not user:
        return jsonify({"message": "User not found"}), 404  
    access_token = ''
    if user['role'] == 'admin':
        access_token = create_access_token(identity='admin')
    else:
        access_token = create_access_token(identity= username)
        
    return jsonify(access_token=access_token), 200


    
