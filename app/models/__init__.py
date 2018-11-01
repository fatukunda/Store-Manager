import psycopg2
from app.db.config_db import connect, commit_to_db
import psycopg2.extras

""" Create json-like output from the database data"""
def make_json(products):
    for product in products:
        product_details = {
            'product_id': product[0],
            'name': product[1],
            'category': product[2],
            'quantity': product[3],
            'in_stock': product[4]
        }
    return product_details

""" Search for a single product"""
def search_single_product(product_id):
        sql =  "SELECT * FROM products WHERE product_id = '{0}'".format(product_id)
        cursor = execute(sql)
        searched_product = cursor.fetchone()
        return searched_product

def execute(sql):
        conn = connect('store_manager_db')
        cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(sql)
        conn.commit()
        return cursor
def search_sales_person(sales_person_id):
    sql = "SELECT * FROM users WHERE user_id = {}".format(sales_person_id)
    cursor = execute(sql)
    sales_person = cursor.fetchone()
    return sales_person