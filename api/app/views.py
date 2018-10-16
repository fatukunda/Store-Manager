# views.py

from flask import Flask, request, jsonify
from  .products import products
from app import app

@app.route('/api/v1/products')
def get_products():
    return jsonify(products)

# Get a single product GET/api/v1/products/<id>
@app.route("/api/v1/products/<id>")
def get_product(id):
    product_list = []
    for product in products:
        for key in product:
            if product[key] == id:
                product_list.append(product)
    return jsonify(product_list)