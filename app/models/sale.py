import uuid
import time

class Sale:
    unit_price=0.00
    total_price=0.00
    quantity_sold = 0

    def __init__(self, sold_item=None, sales_attendant=None, sale_date=time.ctime(), id=str(uuid.uuid4())):
        self.sold_item =sold_item
        self.sales_attendant=sales_attendant
        self.sale_date = sale_date
        self.id = id
