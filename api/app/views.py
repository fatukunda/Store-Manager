# views.py

from flask import Flask, request, jsonify
from  .products import products
from app import app

@app.route('/api/v1/products')
def get_products():
    return jsonify(products)