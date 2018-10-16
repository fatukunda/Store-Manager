# product_views.py
import uuid
from flask import Flask, request, jsonify
from app.models.products import products
from app import app

@app.route('/api/v1/products')
def get_products():
    return jsonify(products)