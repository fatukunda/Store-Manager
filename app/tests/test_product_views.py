from flask import request
import unittest
from app import app
from app.models.products import products


class TestProductViews(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def test_admin_or_attendant_can_get_products(self):
        res = self.client().get('http://localhost:5000/api/v1/products')
        self.assertEqual(200, res.status_code)