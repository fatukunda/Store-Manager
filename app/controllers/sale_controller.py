from app.models import search_single_product, search_sales_person
from app.db.config_db import commit_to_db, connect
from app.models.sale import Sale
from app.models import execute


def make_a_sale(sale_item_id, sales_person_id, quantity_sold):
    product = search_single_product(sale_item_id)
    sale = Sale(sales_person_id, sale_item_id, quantity_sold)
    sql = """INSERT INTO sales(sales_person_id, sale_date, quantity_sold, product_sold_id, total_price)
            VALUES(%s, %s, %s, %s, %s) RETURNING sales_person_id, sale_date, quantity_sold, product_sold_id, total_price;"""
    
    total_price = product[4] * quantity_sold
    quantity_in_stock = product[3]
        
    if quantity_sold > quantity_in_stock:
        return "Not enough products in the store. Sale cannot be made"
    
        
    conn = connect('store-manager-db')
    cursor = conn.cursor()

    cursor.execute(sql, (sale.sales_person,sale.date, sale.quantity_sold, sale.sold_item, total_price))
    product = cursor.fetchone()
    sql_update_product = "UPDATE products SET quantity = {}".format(quantity_in_stock - sale.quantity_sold)
    cursor.execute(sql_update_product)
    commit_to_db(conn, cursor)
    return product

 
def get_all_sales(user_id = None):
    sql =  ""
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

def get_sale_details(sale_id):
    sql ="SELECT * FROM sales WHERE sale_id = {};".format(sale_id)
    cursor = execute(sql)
    sale = cursor.fetchone()
    sale_details = {
        'sales_person': sale[1],
        'sale_date': sale[2],
        'quantity_sold': sale[3],
        'product_sold': sale[4],
        'total_price': sale[5]
    }
    return sale_details