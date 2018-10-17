import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products
from app.models.sales import sales


#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')

@bp.route('/admin/sales')
def get_sales():
    return jsonify(sales)