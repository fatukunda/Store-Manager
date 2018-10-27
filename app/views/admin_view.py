from flask import jsonify, Blueprint, Response, abort, request
from app.models.store import Store
from app.shared import search

bp = Blueprint('admin_view', __name__, url_prefix='/api/v1/admin')

""" Create a store"""
store = Store()

""" Admin panel index view"""
@bp.route('/')
def admin_panel():
    return 'Welcome to the admin panel'

""" Get all products in the store"""
@bp.route('/products', methods = ['GET'])
def get_products():
    products = store.view_all_products()
    if products:
        return jsonify(products)
    else:
        return jsonify({'message' : 'No products in the store'})

""" Get details of a single product"""
@bp.route('/products/<product_id>', methods=['GET'])
def get_single_product(product_id):
    product = store.view_product_detail(product_id)
    if product:
        return jsonify(product)
    else:
        return Response('Product ' + product_id + ' was not found', status=404)

""" Delete a specific product"""
@bp.route('/products/<product_id>', methods=['DELETE'])
def delete_single_product(product_id):
    product_to_delete =  store.delete_product(product_id)
    if product_to_delete:
        return Response('Product deleted successfully', status=202)

""" Add a product"""
@bp.route('/products', methods= ['POST'])
def add_a_product():
    product = store.create_product()
    request_data = request.get_json()
    product.name = request_data['name']
    product.category = request_data['category']
    product.price = request_data['price']
    product.quantity_in_stock = request_data['quantity']
    product.in_stock = request_data['in_stock']

    product_details = {
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'quantity': product.quantity_in_stock,
        'price': product.price,
        'in_stock': product.in_stock
        }
    # Check if the product exists in the list, if not add it. If it exists, return an error message
    search_product = search(product.id, store.products)
    if not search_product:
        store.products.append(product_details)
        return Response('Product ' + product.id + ' has been created', status=201)
    else:
        return 'Product with an id of ' + product.id + ' already exists'

""" Edit a given product"""
@bp.route('/products/<product_id>', methods=['PUT'])
def edit_product(product_id):
    product = search(product_id, store.products)
    if product:
        product = product[0]
        request_data = request.get_json()
        new_product_details = {
            'name': request_data['name'],
            'category': request_data['category'],
            'quantity': request_data['quantity'],
            'price': request_data['price'],
            'in_stock': request_data['in_stock']
        }
        product['name'] = new_product_details['name']
        product['category'] = new_product_details['category']
        product['quantity'] = new_product_details['quantity']
        product['price'] = new_product_details['price']
        product['in_stock'] = new_product_details['in_stock']

        return jsonify(product)
    else:
        return Response('Product '+ product_id + ' was not found', status=404)
    
    
""" View a list of attendants"""
@bp.route('/attendants')
def get_all_attendants():
    if store.view_attendants():
        return jsonify(store.view_attendants())
    else:
        return jsonify({'message': 'No attendants yet. Aadd some'})

""" View attendant details"""
@bp.route('/attendants/<attendant_id>', methods=['GET'])
def get_attendant_details(attendant_id):
    attendant = store.view_attendant_details(attendant_id)
    if attendant:
        return jsonify(attendant)
    else:
        return Response('Attendant ' + attendant_id + ' was not found', status=404)

"Delete attendant"
@bp.route('/attendants/<attendant_id>', methods=['DELETE'])
def delete_attendant(attendant_id):
    attendant_to_delete =  store.delete_store_attendant(attendant_id)
    if attendant_to_delete:
        return Response('Attendant deleted successfully', status=202)


@bp.route('/attendants', methods= ['POST'])
def add_an_attendant():
    attendant = store.create_attendant()
    request_data = request.get_json()
    attendant.first_name = request_data['first_name']
    attendant.last_name = request_data['last_name']
    attendant.username = request_data['username']
    attendant.email = request_data['email']
    attendant.password = request_data['password']

    attendant_details = {
        'id': attendant.id,
        'first_name': attendant.first_name,
        'last_name': attendant.last_name,
        'username': attendant.username,
        'user_type': attendant.user_type,
        'email': attendant.email,
        'sales_made': attendant.sales_made
        }
    # Check if the attendant exists in the list, if not add him. If he exists, return an error message
    search_attendant = search(attendant.id, store.sales_attendants)
    if not search_attendant:
        store.sales_attendants.append(attendant_details)
        return Response('Attendant ' + attendant.id + ' has been created', status=201)
    else:
        return 'Attendant with an id of ' + attendant.id + ' already exists'

""" Edit a given attendant"""
@bp.route('/attendants/<attendant_id>', methods=['PUT'])
def edit_attendant(attendant_id):
    attendant = search(attendant_id, store.sales_attendants)
    if attendant:
        attendant = attendant[0]
        request_data = request.get_json()
        new_attendant_details = {
            'first_name': request_data['first_name'],
            'last_name': request_data['last_name'],
            'email': request_data['email'],
            'username': request_data['username'],
            'user_type': request_data['user_type'],
            'password': request_data['password']
        }
        attendant['first_name'] = new_attendant_details['first_name']
        attendant['last_name'] = new_attendant_details['last_name']
        attendant['email'] = new_attendant_details['email']
        attendant['username'] = new_attendant_details['username']
        attendant['user_type'] = new_attendant_details['user_type']

        return jsonify(attendant)
    else:
        return Response('Attendant '+ attendant_id + ' was not found', status=404)

""" Get a list of all sales made"""
@bp.route('/attendants/sales')
def get_all_sales():
    sales = store.view_sales()
    if sales:
        return jsonify(sales)
    else:
        return jsonify({'message': 'No sales made yet'})

""" View details of a single sale"""
@bp.route('/attendants/sales/<sale_id>')
def get_single_sale(sale_id):
    sale = store.view_sale_details(sale_id)
    if sale:
        return jsonify(sale)
    else:
        return Response('Sale '+ sale_id + ' was not found', status=404)

""" Sort sales by sales person"""
@bp.route('/attendants/<attendant_id>/sales')
def sort_sales_by_sales_attendant(attendant_id):
    sales = store.view_sales_by_attendant(attendant_id)
    if sales:
        return jsonify(sales)
    else:
        return jsonify({'message': 'No sales have been made by attendant ' + attendant_id})

""" Make an attendant an admin"""
@bp.route('/attendants/<attendant_id>/permissions')
def make_admin(attendant_id):
   return jsonify(store.make_attendant_admin(attendant_id))
