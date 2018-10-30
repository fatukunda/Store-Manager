from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, Response, jsonify
from app.models.product import Product


bp = Blueprint('products_view', __name__, url_prefix='/api/v1/products')

""" PRODUCT ROUTES"""
# Add a product to the inventory
@bp.route('', methods=['POST'])
# @jwt_required
def add_product():
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
        product = Product()
        product.name = request_data['name']
        product.category = request_data['category']
        product.quantity = request_data['quantity']
        product.price = request_data['unit_price']
        product.in_stock = request_data['in_stock']
        product.create_product()
        return jsonify("Product created successfully")
       

""" Delete a specific product"""
@bp.route('/<product_id>', methods =['DELETE'])
# @jwt_required
def delete_product(product_id):
    rows_deleted = Product.delete_product(product_id)
    if rows_deleted != -1:
        return 'Product deleted successfully'

""" Edit a specific product"""
@bp.route('/<product_id>', methods =['PUT'])
@jwt_required
def edit_product(product_id):
    request_data = request.get_json()
    name = request_data['name']
    category = request_data['category']
    quantity = request_data['quantity']
    price = request_data['unit_price']
    in_stock = request_data['in_stock']
    rows_edited = Product.edit_product(product_id, name, category, quantity, price, in_stock)
    if rows_edited != -1:
            return jsonify({"message": rows_edited + ' have been updated'})

# Get all products in the store
@bp.route('', methods= ['GET'])
# @jwt_required
def get_products():
        # current_user = get_jwt_identity()
        # return jsonify(logged_in_as=current_user), 200
        return jsonify(Product.get_all_products()), 200

# Get a single product
@bp.route('/<product_id>', methods=['GET'])
@jwt_required
def get_single_product(product_id):
        product = Product.search_single_product(product_id)
        if product:
                return jsonify(product)
        else:
                jsonify({"message": "Product with an Id of "+ product_id + " was not found"}), 404

