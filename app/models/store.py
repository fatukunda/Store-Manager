import psycopg2
from app.db.config_db import connect
from app.db.config_db import commit_to_db
class Store:
    def __init__(self, products=[], sales=[], attendants=[], admins=[]):
        self.products =products
        self.attendants=attendants
        self.sales=sales
        self.admins=admins
    """ Create json-like output from the database data"""
    def make_json(self, products):
        for product in products:
            product_details = {
                'product_id': product[0],
                'name': product[1],
                'category': product[2],
                'quantity': product[3],
                'in_stock': product[4]
            }
        return product_details


    """ Create a new product"""
    def create_product(self, name, category, quantity, price, in_stock):
        """ insert a new product into the products table """
        sql = """INSERT INTO products(name, category, quantity, unit_price, in_stock)
                 VALUES(%s, %s, %s, %s, %s) RETURNING product_id, name, quantity, unit_price, in_stock;"""
        conn = None
        product = None
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (name, category, quantity, price, in_stock))
        product = cursor.fetchone()
        commit_to_db(conn, cursor)
        return product

    """ Get all products in the store """
    def get_all_products(self):
        sql = """ SELECT * FROM products;"""
        conn = None
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        self.products = []
        products = cursor.fetchall()
        for product in products:
            product_details = {
                'id': product[0],
                'name': product[1],
                'category': product[2],
                'quantity': product[3],
                'unit_price': product[4],
                'in_stock': product[5]
            }
            self.products.append(product_details)
        commit_to_db(conn, cursor)
        return self.products

    """ Get all sales made """
    def get_all_sales(self):
        sql = """ SELECT * FROM sales;"""
        conn = None
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        self.sales = []
        sales = cursor.fetchall()
        for sale in sales:
            sale_details = {
                'sale_id': sale[0],
                'sales_person_id': sale[1],
                'sale_date': sale[2],
                'quantity_sold': sale[3],
                'product_sold': sale[4],
                'total_price': sale[5]
            }
            self.products.append(sale_details)
        commit_to_db(conn, cursor)
        return self.sales

    """ Search for a single product given the id"""
    def search_single_product(self, product_id):
        sql =  "SELECT * FROM products WHERE product_id = '{0}'".format(product_id)
        conn = connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            searched_product = cursor.fetchall()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        product_details =  self.make_json(searched_product)
        commit_to_db(conn, cursor)
        return product_details

    """ Create a store attendant"""
    def create_attendant(self, first_name, last_name, username, email, password, usertype):
        """ insert a new attendant into the users table """
        sql = """INSERT INTO users(first_name, last_name, username, email, password, usertype)
                 VALUES(%s, %s, %s, %s, %s, %s) RETURNING user_id, first_name, last_name, email, usertype;"""
        conn = None
        user = None
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (first_name, last_name, username, email, password, usertype))
        user = cursor.fetchone()
        commit_to_db(conn, cursor)
        return user

    """ Create a sale"""
    def create_sale(self, sales_person_id, sale_date, quantity_sold, product_sold_id, total_price):
        """ Search for a product and get the unit price"""
        product = self.search_single_product(product_sold_id)
        # Get unit_price and multiply by quantity sold
        unit_price = product[4]
        total_price = unit_price * quantity_sold
        """ insert a new sale into the sales table """
        sql = """INSERT INTO sales(sales_person_id, sale_date, quantity_sold, product_sold_id, total_price)
                 VALUES(%s, %s, %s, %s, %s) RETURNING sale_id, sales_person_id, sale_date, quantity_sold, product_sold_id, total_price;"""
        conn = None
        sale = None
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (sales_person_id, sale_date, quantity_sold, product_sold_id, total_price))
        sale = cursor.fetchone()
        """ Reduce the quantity of the products in the store"""
        product[3] -= quantity_sold
        """ commit changes and close the database connection"""
        commit_to_db(conn, cursor)
        return sale

