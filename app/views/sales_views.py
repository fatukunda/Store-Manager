import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products
from app.models.sales import sales


#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')

# Get all sales by the admin
@bp.route('/admin/sales')
def get_sales():
    return jsonify(sales)

# Get a single sale by admin
@bp.route('/admin/sales/<id>')
def admin_get_single_sale(id):
    sale_list = []
    for sale in sales:
        for key in sale:
            if sale[key] == id:
                sale_list.append(sale)
    return jsonify(sale_list)

# Get all sales made by a particular store attendant
@bp.route('attendants/<username>/sales')
def attendant_get_sales(username):
    sale_list = []
    for sale in sales:
        for key in sale:
            if sale[key] == username:
                sale_list.append(sale)
    return jsonify(sale_list)

# Get a single sale made by a specific attendant
@bp.route('attendants/<username>/sales/<id>')
def attendant_get_single_sale(username, id):
    pass