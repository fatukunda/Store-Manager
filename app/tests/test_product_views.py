from flask import request, json
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
def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    res =  json.loads(response.data.decode('utf8'))
    return [res]

def get_id(product):
    prod = None
    for item in products:
        for key in item:
            if item[key] == product.id:
                prod = item
    return prod.get('id')

# test GET/api/v1/products
def test_get_products_returns_all_products(client):
    with client:
        res = client.get('/api/v1/products')
        assert res.status_code == 200
        assert json_of_response(res)

# test GET/api/v1/products/<id>    
def test_get_single_product_returns_a_product(client):
    with client:
        res = client.get('/api/v1/products/<id>')
        assert res.status_code == 200
        assert json_of_response(res)
        assert len(json_of_response(res)) == 1
        
# Test POST/api/v1/admin/products
def test_add_product_adds_a_product(client):
    product = Product('17 inch Toshiba Laptop', 'Laptops', 10, 1600000.00)
    with client:
        number_of_products = len(products)
        res = client.post('api/v1/admin/products', data = json.dumps(dict(
            id = product.id,
            name = product.name,
            category = product.category,
            quantity = product.quantity,
            price = product.quantity

        )) , content_type ='application/json')
        assert product.id in products[3]['id']
        assert res.status_code == 200
        assert len(products) > number_of_products
        
            
