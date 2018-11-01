from flask import json
from flask_jwt_extended import create_access_token
import pytest
from app.controllers import sale_controller
from app import app
from app.models.sale import Sale
""" SALES TESTS"""

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# # Test GET/api/v1/admin/sales
# def test_get_sales_returns_all_sales(client):
#     with client:
#         res = client.get('/api/v1/sales')
#         assert res.status_code == 200
#         assert json_response(res)

# # Test GET/api/v1/admin/sales/<id>    
# def test_get_single_sale_returns_a_sale(client):
#     with client:
#         res = client.get('/api/v1/sales/<id>')
#         assert res.status_code == 200
#         assert json_response(res)
#         assert len(json_response(res)) == 1

# # Test GET/api/v1/attendants/<username>/sales
# def test_attendant_get_sales(client):
#     with client:
#         res = client.get('/api/v1/attendants/<attendant_id>/sales')
#         assert res.status_code == 200
#         assert json_response(res)

# # Test GET/api/v1/attendants/<username>/sales/<id>
# def test_get_single_sale_for_attendant(client):
#     with client:
#         res = client.get('api/v1/attendants/<username>/sales/<id>')
#         assert res.status_code == 200
#         assert json_response(res)
#         assert len(json_response(res)) == 1