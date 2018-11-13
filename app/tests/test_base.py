import pytest
import unittest
from app.db.config_db import connect
from app import create_app

app = create_app('test')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app     
        self.app.config['ENV'] = 'testing'   
        self.conn = connect()      
        self.client = self.app.test_client(self)
        self.user = dict(
            username='fatukunda',
            password='admin123'
        )
        self.user = dict(
            username='slee',
            password='ab123'
        )
        self.sale_data = dict(
            product_sold=1,
            quantity=4
        )
    
    def tearDown(self):
        self.conn.drop_relation('users')
        self.conn.drop_relation('products')
        self.conn.drop_relation('sales')