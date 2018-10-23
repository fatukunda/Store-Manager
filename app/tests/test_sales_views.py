from flask import request, json
import pytest
from app.models.sales import sales, Sale
from app import app
import uuid

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


# Helper methods
def json_response(response):
    """Decode json from response"""
    res =  json.loads(response.data.decode('utf8'))
    return [res]

# Test GET/api/v1/admin/sales
def test_get_sales_returns_all_sales(client):
    with client:
        res = client.get('/api/v1/admin/sales')
        assert res.status_code == 200
        assert json_response(res)

# Test GET/api/v1/admin/sales/<id>    
def test_get_single_sale_returns_a_sale(client):
    with client:
        res = client.get('/api/v1/admin/sales/<id>')
        assert res.status_code == 200
        assert json_response(res)
        assert len(json_response(res)) == 1
# Test GET/api/v1/attendants/<username>/sales
def test_attendant_get_sales(client):
    with client:
        res = client.get('/api/v1/attendants/<username>/sales')
        assert res.status_code == 200
        assert json_response(res)

# Test GET/api/v1/attendants/<username>/sales/<id>
def test_get_single_sale_for_attendant(client):
    with client:
        res = client.get('/api/v1/attendants/<username>/sales/<id>')
        assert res.status_code == 200
        assert json_response(res)
        assert len(json_response(res)) == 1

# Test POST/api/v1/attendant/<username>/sales
def test_add_sale_adds_a_sale(client):
    sale = Sale()
    sale.sales_person = 'jJackson'
    sale.sold_item = '17 inch Toshiba Laptop'   
    sale.quantity_sold = 1
    sale.unit_price = 1600000.00
    sale.total_price = 1600000.00 
    with client:
        number_of_sales = len(sales)
        res = client.post('api/v1/attendants/<username>/sales', data = json.dumps(dict(
            date = sale.date,
            id = sale.id,
            quantity_sold = sale.quantity_sold,
            sales_person = sale.sales_person,
            sold_tem = sale.sold_item,
            total_price = sale.total_price,
            unit_price = sale.unit_price
        )) , content_type ='application/json')
        assert sale.id in sales[3]['id']
        assert res.status_code == 200
        assert len(sales) > number_of_sales
        
            
