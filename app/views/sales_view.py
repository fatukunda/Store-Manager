from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.views import create_store
from app.models.sale import Sale

bp = Blueprint('sales_view', __name__, url_prefix='/api/v1/sales')


store = create_store()

""" SALE ROUTES"""
# Get all sales by the admin
@bp.route('')
def get_sales():
    return jsonify(Sale.get_all_sales())

# Get a single sale by admin
@bp.route('/<id>')
def admin_get_single_sale(id):
   pass

# Get all sales made by a particular store attendant
@bp.route('/<attendant_id>')
def attendant_get_sales(attendant_id):
    return jsonify(Sale.get_all_sales(attendant_id))

# Get a single sale made by a specific attendant
@bp.route('/<attendant_id>/sales/<sale_id>')
def get_single_sale(attendant_id, sale_id):
    pass


# Attendant make a sale
@bp.route('', methods=['POST'])
def make_sale():
    sale = Sale()
    request_data = request.get_json()
    sale.sold_item = request_data['product_id']
    sale.quantity_sold = request_data['quantity_sold']
    sale.sales_person = request_data['sales_person']
    sale.make_a_sale()
    return jsonify({"message" : "Sale successfully completed"}), 201

""" Get sale details"""
@bp.route('/<attendant_id>/sales/<sale_id>')
def get_a_single_sale(sale_id):
        pass
