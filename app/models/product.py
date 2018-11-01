import psycopg2
from app.db.config_db import connect, commit_to_db
from app.models import make_json, search_single_product, execute

class Product:
    in_stock = True
    def __init__(self, category='', name = '', quantity=0, unit_price=0.00):
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.name = name

    def __dict__(self):
        """
	    Serialize product into json form
		"""
        return { 'name': self.name, 
                'category': self.category, 
                'quantity': self.quantity,
                'unit_price': self.unit_price}

    def create(self, sql):
        cursor = execute(sql)
        return cursor

    def delete(self, sql):
        cursor = execute(sql)
        return cursor








    