import psycopg2
from app.db.config_db import connect, commit_to_db
from app.models import make_json, search_single_product, execute
class Product:
    in_stock = False
    def __init__(self, category='', name = '', quantity=0, price=0.00):
        self.category = category
        self.quantity = quantity
        self.price = price
        self.name = name