from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, Response, jsonify
from app.controllers import product_controller


bp = Blueprint('products_view', __name__, url_prefix='/api/v1/products')

""" PRODUCT ROUTES"""
# Add a product to the inventory
@bp.route('', methods=['POST'])
@jwt_required
def add_product():
        current_user = get_jwt_identity()
        if current_user == 'admin':
                if not request.is_json:
                        return jsonify({"message": "Request is missing json"}), 400 
                request_data = request.get_json()
                if not isinstance(request_data['name'], str):
                        return jsonify({"message": "Product name should be a string"})
                if not isinstance(request_data['category'], str):
                        return jsonify({"message": "Product name should be a string"})
                if not isinstance(request_data['quantity'], int):
                        return jsonify({"message": "Quantity should be a number"})
                if not isinstance(request_data['in_stock'], bool):
                        return jsonify({"message": "in_stock should be a true or false"})
        
                name = request_data['name']
                category = request_data['category']
                quantity = request_data['quantity']
                price = request_data['unit_price']
                in_stock = request_data['in_stock']
                product_controller.create_product(name, category, quantity, price, in_stock)
                return jsonify("Product created successfully"), 201
        else:
                return jsonify({"message": "Not authorized to access this route"}), 401
       

""" Delete a specific product"""
@bp.route('/<product_id>', methods =['DELETE'])
@jwt_required
def delete_product(product_id):
        current_user = get_jwt_identity()
        if current_user == 'admin':
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
        if current_user == 'admin':
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

