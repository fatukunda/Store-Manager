import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products
from app.models.sales import sales


#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')

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