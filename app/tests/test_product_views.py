from flask import json
import pytest
from app.models.products import products, Product
from app import app
import uuid

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


# Helper methods

def json_response(response):
    """Covert response to json"""
    res =  json.loads(response.data.decode('utf8'))
    return [res]

# test GET/api/v1/products
def test_get_products_returns_all_products(client):
    with client:
        res = client.get('/api/v1/products')
        assert res.status_code == 200
        assert json_response(res)

# test GET/api/v1/products/<id>    
def test_get_single_product_returns_a_product(client):
    with client:
        res = client.get('/api/v1/products/<id>')
        assert res.status_code == 200
# Test POST/api/v1/admin/products
def test_add_product_adds_a_product(client):
    product = Product('Laptops', 10, 1600000.00)
    product.name = '17 inch Toshiba Laptop'
    with client:
        number_of_products = len(products)
        res = client.post('api/v1/admin/products', data = json.dumps(dict(
            id = product.id,
            name = product.name,
            category = product.category,
            quantity = product.quantity,
            price = product.quantity

        )) , content_type ='application/json')
        product_details = {
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'quantity': product.quantity,
        'price': product.price
        }
        products.append(product_details)
        assert product.id in products[3]['id']
        assert res.status_code == 201
        assert len(products) > number_of_products
        
            
