# product_views.py
import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

@bp.route('/products', methods= ['GET'])
def get_products():
    return jsonify(products)
