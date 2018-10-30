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

    """ Create a new product"""
    def create_product(self):
        """ insert a new product into the products table """
        sql = """INSERT INTO products(name, category, quantity, unit_price, in_stock)
                 VALUES(%s, %s, %s, %s, %s) RETURNING product_id, name, quantity, unit_price, in_stock;"""
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (self.name, self.category, self.quantity, self.price, self.in_stock))
        product = cursor.fetchone()
        commit_to_db(conn, cursor)
        return product

    """ Get all products in the store """
    @staticmethod
    def get_all_products():
        sql = """ SELECT * FROM products;"""
        conn = None
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        products = cursor.fetchall()
        products_list = []
        for product in products:
            product_details = {
                'id': product[0],
                'name': product[1],
                'category': product[2],
                'quantity': product[3],
                'unit_price': product[4],
                'in_stock': product[5]
            }
            products_list.append(product_details)
        commit_to_db(conn, cursor)
        return products_list

    """ Get a single product"""
    @staticmethod
    def search_single_product(product_id):
        searched_product = search_single_product(product_id)
        product_details = {
            'id': searched_product[0],
            'name': searched_product[1],
            'category': searched_product[2],
            'quantity': searched_product[3],
            'unit_price': searched_product[4],
            'in_stock': searched_product[5]
            }
        return product_details
    
    """ Delete a product from the store"""
    @staticmethod
    def delete_product(product_id):
        sql = "DELETE FROM products WHERE product_id = {0};".format(product_id)
        rows_deleted = 0
        cursor = execute(sql)
        rows_deleted = cursor.rowcount
        return rows_deleted
    
    """ Edit a specific product"""
    @staticmethod
    def edit_product(product_id, name, category, quantity, unit_price, in_stock):
        sql = """UPDATE products SET
        name = {0}
        category = {1}
        quantity = {2}
        unit_price = {3}
        in_stock = {4} WHERE product_id = {5}
        """.format(name, category, quantity, unit_price, in_stock, product_id)
        rows_edited = 0
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_edited = cursor.rowcount
        commit_to_db(conn, cursor)
        return rows_edited





    