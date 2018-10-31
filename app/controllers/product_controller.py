from app.models.product import Product
from app.db.config_db import commit_to_db, connect
from app.models import search_single_product, execute

def create_product(name, category, quantity, price, in_stock):
    """ insert a new product into the products table """
    sql = """INSERT INTO products(name, category, quantity, unit_price, in_stock)
                 VALUES(%s, %s, %s, %s, %s) RETURNING product_id, name, quantity, unit_price, in_stock;"""
    conn = connect('store-manager-db')
    cursor = conn.cursor()
    cursor.execute(sql, (name, category, quantity, price, in_stock))
    product = cursor.fetchone()
    commit_to_db(conn, cursor)
    return product
   
def get_all_products():
    """ Get all products in the store """
    sql = """SELECT * FROM products;"""
    conn = connect('store-manager-db')
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

def search_a_product(product_id):
    """ Get a single product"""
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
def delete_product(product_id):
    sql = "DELETE FROM products WHERE product_id = {0};".format(product_id)
    rows_deleted = 0
    cursor = execute(sql)
    rows_deleted = cursor.rowcount
    return rows_deleted

def edit_product(product_id, name, category, quantity, unit_price, in_stock):
    """ Edit a specific product"""
    sql = """UPDATE products SET
    name = {0}
    category = {1}
    quantity = {2}
    unit_price = {3}
    in_stock = {4} WHERE product_id = {5}
    """.format(name, category, quantity, unit_price, in_stock, product_id)
    rows_edited = 0
    conn = connect('store-manager-db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rows_edited = cursor.rowcount
    commit_to_db(conn, cursor)
    return rows_edited