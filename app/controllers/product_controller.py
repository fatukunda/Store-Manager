from app.models.product import Product
from app.db.config_db import commit_to_db, connect
from app.models import search_single_product, execute
from app.models.product import Product

def create_product(name, category, quantity, price):
    """ insert a new product into the products table """
    product = Product(category, name, quantity, price)
    sql = """INSERT INTO products (name, category, quantity, unit_price, in_stock)
                 VALUES({0}, {1}, {2}, {3}, {4}) RETURNING product_id, name, quantity, unit_price, in_stock;""".format(product.name, product.quantity, product.category, product.unit_price, product.in_stock)
    
    cursor = execute(sql)
    product = cursor.fetchone()
    # commit_to_db(conn, cursor)
    return product
   
def get_all_products():
    """ Get all products in the store """
    sql = """SELECT * FROM products;"""
    cursor =execute(sql)
    products = cursor.fetchall()
    return products

def search_a_product(product_id):
    """ Get a single product"""
    return search_single_product(product_id)
    

""" Delete a product from the store"""
def delete_product(product_id):
    sql = "DELETE FROM products WHERE product_id = {0};".format(product_id)
    rows_deleted = 0
    cursor = execute(sql)
    rows_deleted = cursor.rowcount
    return rows_deleted

def edit_product(product_id, quantity, unit_price):
    """ Edit a specific product"""
    sql = """UPDATE products SET
    quantity = {0},
    unit_price = {1}
    WHERE product_id = {2}
    """.format(quantity, unit_price, product_id)
    rows_edited = 0
    cursor = execute(sql)
    rows_edited = cursor.rowcount
    return rows_edited