import uuid
from time import ctime
from app.db.config_db import connect, commit_to_db
from app.models import search_sales_person, search_single_product
from flask import jsonify

class Sale:
    total_price = 0.00
    def __init__(self, sales_person = '', sold_item ='', quantity_sold= 0, date =ctime()):
        self.sales_person = sales_person
        self.sold_item = sold_item
        self.quantity_sold = quantity_sold
        self.date = date
    