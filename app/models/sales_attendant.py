import uuid
from app.models.sale import Sale
from app.shared import search
class SalesAttendant:
    sales_made = []
    first_name =''
    last_name =''
    user_type = 'user'
    def __init__(self, username='', email='', password='', id=str(uuid.uuid4())):
        
        self.username=username
        self.email=email
        self.password=password
        self.id=id

    # def make_a_sale(self, product_to_sale, quantity_to_sale, products):
    #     """ Check if the product is in stock before making a sale"""

    #     sale = Sale(product_to_sale, self)
    #     sale.unit_price = product_to_sale.price
    #     sale.quantity_sold = quantity_to_sale
    #     sale.total_price = product_to_sale.price * quantity_to_sale
    #     """ Go through a list of products and decrease its quantity by the quantity sold"""
    #     for product in products:
    #         for key in product:
    #             if product[key] == product_to_sale.id:
    #                 product['quantity_in_stock'] -= quantity_to_sale
    #             else:
    #                 return 'Product not found'

    #     """ Add the sale to a list of attendant's sales"""
    #     self.sales_made.append(sale)
    #     return sale

    """ View details of a single sale made by the attendant"""
    def view_sale_details(self, sale_id):
        sale = search(sale_id, self.sales_made)
        if sale:
            return sale
        return 'No such sale was made by you'

    """ Get the total sales made by an attendant"""
    def calculate_sales_made(self):
        total_sales_made = len(self.sales_made)
        return total_sales_made