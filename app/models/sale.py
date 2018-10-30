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

    def make_a_sale(self):
        product = search_single_product(self.sold_item)
        sales_person = search_sales_person(self.sales_person)
#    insert a new sale into the sales table 
        sql = """INSERT INTO sales(sales_person_id, sale_date, quantity_sold, product_sold_id, total_price)
                VALUES(%s, %s, %s, %s, %s) RETURNING sales_person_id, sale_date, quantity_sold, product_sold_id, total_price;"""
        
        conn = connect('store-manager-db')
        cursor = conn.cursor()
        total_price = product[4] * self.quantity_sold
        quantity_in_stock = product[3]
        
        if self.quantity_sold > quantity_in_stock:
            return jsonify({"message": "Not enough products in the store. Sale cannot be made"}), 400

        cursor.execute(sql, (self.sales_person, self.date, self.quantity_sold, self.sold_item, total_price))
        product = cursor.fetchone()
        sql_update_product = "UPDATE products SET quantity = {}".format(quantity_in_stock - self.quantity_sold)
        cursor.execute(sql_update_product)
        commit_to_db(conn, cursor)
        return product

    @staticmethod  
    def get_all_sales(user_id = None, sql = ""):
        if user_id:
            sql = "SELECT * FROM sales WHERE sales_person_id = {};".format(user_id)
        else:
            sql = """SELECT * FROM sales;"""
        conn = connect('store-manager-db')
        cursor = conn.cursor()
        cursor.execute(sql)
        sales = cursor.fetchall()
        sale_list = []
        for sale in sales:
            product = search_single_product(sale[4])
            attendant = search_sales_person(sale[1])
            sale_details = {
                'sales_person': attendant[1],
                'sale_date': sale[2],
                'quantity_sold': sale[3],
                'product_sold': product[1],
                'unit_price': product[4],
                'total_price': sale[5]
            }
            sale_list.append(sale_details)
        commit_to_db(conn, cursor)
        return sale_list
    