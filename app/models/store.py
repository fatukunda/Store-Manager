from flask import jsonify
from app.models.sales_attendant import SalesAttendant
from app.models.product import Product
from app.models.sale import Sale
from app.shared import search, delete, edit

class Store():
    def __init__(self, products=[], sales=[], sales_attendants=[], admins =[]):
        self.products = products
        self.sales = sales
        self.sales_attendants=sales_attendants
        self.admins = admins

    """ Create a new attendant and add him to the list of attendants"""
    def create_attendant(self):
        attendant = SalesAttendant()
        return attendant

    """ Give an attendant admin rights"""
    def make_attendant_admin(self, attendant_id):
        attendant = search(attendant_id, self.sales_attendants)
        if attendant:
            attendant = attendant[0]
            attendant['user_type'] = 'admin'
            self.admins.append(attendant)
        return attendant

    """ View all the attendants in the store"""
    def view_attendants(self):
        return self.sales_attendants

    """ Given an attendant id, view their details"""
    def view_attendant_details(self, attendant_id):
        return search(attendant_id, self.sales_attendants)

    """ View a list of sales made"""
    def view_sales(self):
        return self.sales

    """ View sales made by a specific attendant"""
    def view_sales_by_attendant(self, attendant_id):
        attendant = search(attendant_id, self.sales_attendants)
        if attendant:
            return attendant[0].sales_made
    """ View a sale details"""
    def view_sale_details(self, sales_id):
        sale = search(sales_id, self.sales)
        return sale
    """ View all products in the store"""
    def view_all_products(self):
        return self.products

    """ View details of a single product"""
    def view_product_detail(self, product_id):
        return search(product_id, self.products)

    """ Create a new product and add it to a list of products"""
    def create_product(self):
        product = Product()
        return product

    """ Delete a product given the id"""
    def delete_product(self, product_id):
       return delete(product_id, self.products)
    
    """ Delete a store attendant from the store"""
    def delete_store_attendant(self, attendant_id):
       return delete(attendant_id, self.sales_attendants)

    """ Delete a sale from the store"""
    def delete_sale(self, sale_id):
       return delete(sale_id, self.sales)
    
    """ Edit a particular product"""
    def edit_product(self, product_id, new_product_info):
        return edit(product_id, self.products, new_product_info)

    """Edit a particular sale"""
    def edit_sale(self, sale_id, **kwargs):
        return edit(sale_id, self.sales, kwargs)
    
    """Edit a particular sales attendant"""
    def edit_sales_attendant(self, attendant_id, **kwargs):
        return edit(attendant_id, self.sales_attendants, kwargs)

    """ Make a sale"""
    def make_a_sale(self, product_to_sale, quantity_to_sale, sales_attendant):
        """ Check if the product is in stock before making a sale"""
        product = search(product_to_sale, self.products)
        if product:
            product = product[0]
            sale = Sale(product['id'], sales_attendant,)
            sale.unit_price = product['price']
            sale.quantity_sold = quantity_to_sale
            sale.total_price = product['price'] * quantity_to_sale
            """ Decrease product quantity by the quantity sold"""
            print(product)
            product['quantity_in_stock'] -= quantity_to_sale

            """ Add the sale to a list of attendant's sales"""
            sales_attendant.sales_made.append(sale)
            return sale