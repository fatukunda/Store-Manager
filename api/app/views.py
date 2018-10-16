# views.py
import uuid
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

# Add a product POST/api/v1/products
@app.route("/api/v1/products", methods = ['POST'])
def add_product():
    name = request.form.get('name')
    category = request.form.get('category')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    product = {
        'id': str(uuid.uuid4()),
        'name': name,
        'category': category,
        'quantity': int(quantity),
        'price': float(price)
    }
    products.append(product)
    return 'Product %s created successfully' % product['name']