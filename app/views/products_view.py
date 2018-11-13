from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from app.controllers import product_controller
from app.models import search_sales_person


bp = Blueprint('products_view', __name__, url_prefix='/api/v1/products')

""" PRODUCT ROUTES"""
# Add a product to the inventory
@bp.route('', methods=['POST'])
@jwt_required
def add_product():
        current_user = get_jwt_identity()
        user_role = search_sales_person(current_user)
        if user_role['user_type'] == 'admin':
                if not request.is_json:
                        return jsonify({"message": "Request is missing json"}), 400 
                request_data = request.get_json()
                if not isinstance(request_data['name'], str):
                        return jsonify({"message": "Product name should be a string"}), 400
                if not isinstance(request_data['category'], str):
                        return jsonify({"message": "Product name should be a string"}), 400
                if not isinstance(request_data['quantity'], int):
                        return jsonify({"message": "Quantity should be a number"}), 400
                if not isinstance(request_data['unit_price'], int):
                        return jsonify({"message": "The price should be a number"}), 400
        
                name = request_data['name']
                category = request_data['category']
                quantity = request_data['quantity']
                price = request_data['unit_price']
                product_controller.create_product(name, category, quantity, price)
                return jsonify("Product created successfully"), 201
        else:
                return jsonify({"message": "Not authorized to access this route"}), 401
       

""" Delete a specific product"""
@bp.route('/<product_id>', methods =['DELETE'])
@jwt_required
def delete_product(product_id):
        current_user = get_jwt_identity()
        user_role = search_sales_person(current_user)
        if user_role['user_type'] == 'admin':
                rows_deleted = product_controller.delete_product(product_id)    
                if rows_deleted != -1:
                        return 'Product deleted successfully'
        else:
                return jsonify({"message": "Not authorized to access this page"}), 401

""" Edit a specific product"""
@bp.route('/<product_id>', methods =['PUT'])
@jwt_required
def edit_product(product_id):
        current_user = get_jwt_identity()
        user_role = search_sales_person(current_user)
        if user_role['user_type'] == 'admin':
                request_data = request.get_json()
                quantity = request_data['quantity']
                price = request_data['unit_price']
                rows_edited = product_controller.edit_product(product_id, quantity, price)
                if rows_edited != -1:
                        return jsonify("Product has been updated")
        else:
                return jsonify({"message": "Not authorized to access this page"}), 401


# Get all products in the store
@bp.route('/', methods= ['GET'])
@jwt_required
def get_products():
        return jsonify(product_controller.get_all_products()), 200

# Get a single product
@bp.route('/<product_id>', methods=['GET'])
@jwt_required
def get_single_product(product_id):
        product = product_controller.search_single_product(product_id)
        if product:
                return jsonify(product)
        else:
                return jsonify({"message": "Product with an Id of "+ product_id + " was not found"}), 404

