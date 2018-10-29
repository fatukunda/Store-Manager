from flask import json
import pytest
from app.models.products import Product
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

# test GET/api/v1/store/products
def test_get_products_returns_all_products(client):
    with client:
        res = client.get('/api/v1/store/products')
        assert res.status_code == 200
        assert json_response(res)

# test GET/api/v1/store/products/<id>    
def test_get_single_product_returns_a_product(client):
    with client:
        res = client.get('/api/v1/store/products/<id>')
        assert res.status_code == 200

# Test POST/api/v1/attendants/<username>/sales
def test_add_sale_adds_a_sale(client):
    sale = Sale()
    sale.sales_person = 'jJackson'
    sale.sold_item = '17 inch Toshiba Laptop'   
    sale.quantity_sold = 1
    sale.unit_price = 1600000.00
    sale.total_price = 1600000.00 
    with client:
        # number_of_sales = len(sales)
        res = client.post('api/v1/attendants/<username>/sales', data = json.dumps(dict(
            date = sale.date,
            quantity_sold = sale.quantity_sold,
            sales_person = sale.sales_person,
            sold_item = sale.sold_item,
            total_price = sale.total_price,
            unit_price = sale.unit_price
        )) , content_type ='application/json')
        # assert sale.id in sales[3]['id']
        assert res.status_code == 201
        # assert len(sales) > number_of_sales
        
            
