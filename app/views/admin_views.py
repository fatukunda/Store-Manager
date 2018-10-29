# admin_views.py
from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.views import create_store
from app.models.sale import Sale

bp = Blueprint('admin_views', __name__, url_prefix='/api/v1/admin')


store = create_store()

""" PRODUCT ROUTES"""
# Add a product to the inventory
@bp.route('/products', methods=['POST'])
def add_product():
    product = Product()
    request_data = request.get_json()
    product.name = request_data['name']
    product.category = request_data['category']
    product.quantity = request_data['quantity']
    product.price = request_data['price']
    product.in_stock = request_data['in_stock']
    
    store.create_product(product.name, product.category, product.quantity, product.price, product.in_stock)
    return Response('Product %s created successfully' % product.name, status=201)

""" Delete a specific product"""
@bp.route('/products/<product_id>', methods =['DELETE'])
def delete_product(product_id):
    pass

""" Edit a specific product"""
@bp.route('/products/<product_id>', methods =['PUT'])
def edit_product(product_id):
    pass

""" ATTENDANT ROUTES"""

""" Register an attendant"""
@bp.route('/attendants', methods=['POST'])
def register_attendant():
    pass

""" Get a list of attendants in the store"""
@bp.route('/attendants', methods=['GET'])
def get_attendant():
    pass

""" Get details of a single attendant"""
@bp.route('/attendants/<attendant_id>', methods=['GET'])
def get_attendant_details():
    pass

""" Delete an attendant given the Id"""
@bp.route('/attendants/<attendant_id>', methods=['DELETE'])
def delete_attendant(attendant_id):
    pass

""" Edit an attendant given the Id"""
@bp.route('/attendants/<attendant_id>', methods=['PUT'])
def edit_attendant(attendant_id):
    pass

""" SALE ROUTES"""
# Get all sales by the admin
@bp.route('/sales')
def get_sales():
    return jsonify(store.get_all_sales())

# Get a single sale by admin
@bp.route('/sales/<id>')
def admin_get_single_sale(id):
   pass

# Get all sales made by a particular store attendant
@bp.route('attendants/<attendant_id>/sales')
def attendant_get_sales(attendant_id):
    pass

# Get a single sale made by a specific attendant
@bp.route('/attendants/<attendant_id>/sales/<sale_id>')
def attendant_get_single_sale(attendant_id, sale_id):
    pass

