from time import ctime

class Sale:
    total_price = 0.00
    def __init__(self, sales_person = '', sold_item ='', quantity_sold= 0, date =ctime()):
        self.sales_person = sales_person
        self.sold_item = sold_item
        self.quantity_sold = quantity_sold
        self.date = date
    