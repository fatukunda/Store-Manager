from app.models import search_single_product, search_sales_person
from app.db.config_db import commit_to_db, connect
from app.models.sale import Sale
from app.models import execute
import psycopg2.extras
from flask import abort, Response, jsonify

def make_a_sale(sale_item_id, sales_person_id, quantity_sold):
    product = search_single_product(sale_item_id)
    sale = Sale(sales_person_id, sale_item_id, quantity_sold)
    sql = """INSERT INTO sales(sales_person_id, sale_date, quantity_sold, product_sold_id, total_price)
            VALUES(%s, %s, %s, %s, %s) RETURNING sales_person_id, sale_date, quantity_sold, product_sold_id, total_price;"""
    if not product:
        abort(Response("No product with an id of {} in the store".format(sale_item_id)))
    total_price = product['unit_price'] * quantity_sold
    quantity_in_stock = product['quantity']
        
    if quantity_sold > quantity_in_stock:
        abort(jsonify({"message": "Not enough products to make a sale"}))
    if product['quantity'] == 0:
        product['in_stock'] = False
    else:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(sql, (sale.sales_person,sale.date, sale.quantity_sold, sale.sold_item, total_price))
        product = cursor.fetchone()
        sql_update_product = "UPDATE products SET quantity = {0} WHERE product_id = {1}".format(quantity_in_stock - sale.quantity_sold, sale_item_id )
        cursor.execute(sql_update_product)
        commit_to_db(conn, cursor)
        return product

 
def get_all_sales(user_id = None):
    sql =  ""
    if user_id:
        sql = "SELECT * FROM sales WHERE sales_person_id = {};".format(user_id)   
    else:
        sql = """SELECT * FROM sales;"""
    conn = connect()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute(sql)
    sales = cursor.fetchall()
    sale_list = []
    for sale in sales:
        product = search_single_product(sale['product_sold_id'])
        attendant = search_sales_person(sale['sales_person_id'])
        sale_details = {
            'sales_person': attendant['user_id'],
            'sale_date': sale['sale_date'],
            'quantity_sold': sale['quantity_sold'],
            'product_sold': product['product_id'],
            'unit_price': product['unit_price'],
            'total_price': sale['total_price']
        }
        sale_list.append(sale_details)
    commit_to_db(conn, cursor)
    return sale_list

def get_sale_details(sale_id):
    sql ="SELECT * FROM sales WHERE sale_id = {};".format(sale_id)
    cursor = execute(sql)
    sale = cursor.fetchone()
    return sale