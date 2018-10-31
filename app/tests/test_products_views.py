from flask import json
from flask_jwt_extended import create_access_token
import pytest
from app.models.product import Product
from app import app
from app.models.sale import Sale

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
def test_get_products_returns_all_products_not_authorized(client):
    with client:
        res = client.get('/api/v1/products')
        assert res.status_code == 401
        assert json_response(res)

# # test GET/api/v1/products
# def test_get_products_returns_all_products_authorized(client):
#     with client:
#         access_token = create_access_token('admin')
#         headers = {
#                 'Authorization': 'Bearer {}'.format(access_token)
#         }
#         res = client.get('/api/v1/products', headers = headers)
#         assert res.status_code == 200

# test GET/api/v1/products/<id>    
def test_get_single_product_returns_a_product(client):
    with client:
            pass
        # res = client.get('/api/v1/products/<id>')
        # assert res.status_code == 200
        
# Test POST/api/v1/admin/products
def test_add_product_adds_a_product(client):    
    product = Product('Laptops', '17 inch Toshiba Laptop', 10, 1600000.00)
    with client:
            pass
        # # products = []
        # # number_of_products = len(products)
        # res = client.post('api/v1/products', data = json.dumps(dict(
        #     name = product.name,
        #     category = product.category,
        #     quantity = product.quantity,
        #     price = product.quantity

        # )) , content_type ='application/json')
        # product_details = {
        # 'name': product.name,
        # 'category': product.category,
        # 'quantity': product.quantity,
        # 'price': product.price
        # }
        # # products.append(product_details)
        # # assert product.id in products[3]['id']
        # assert res.status_code == 201
        # # assert len(products) > number_of_products

""" SALES TESTS"""

# # Test GET/api/v1/admin/sales
# def test_get_sales_returns_all_sales(client):
#     with client:
#         res = client.get('/api/v1/admin/sales')
#         assert res.status_code == 200
#         assert json_response(res)

# # Test GET/api/v1/admin/sales/<id>    
# def test_get_single_sale_returns_a_sale(client):
#     with client:
#         res = client.get('/api/v1/admin/sales/<id>')
#         assert res.status_code == 200
#         assert json_response(res)
#         assert len(json_response(res)) == 1

# # Test GET/api/v1/attendants/<username>/sales
# def test_attendant_get_sales(client):
#     with client:
#         res = client.get('/api/v1/attendants/<username>/sales')
#         assert res.status_code == 200
#         assert json_response(res)

# # Test GET/api/v1/attendants/<username>/sales/<id>
# def test_get_single_sale_for_attendant(client):
#     with client:
#         res = client.get('api/v1/attendants/<username>/sales/<id>')
#         assert res.status_code == 200
#         assert json_response(res)
#         assert len(json_response(res)) == 1

        
            
