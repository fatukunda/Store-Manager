# """ SALES TESTS"""

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