import uuid
from time import ctime
sales = [
    {
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': 'Simon Lee',
    'sold_item': 'Samsung 32 inch TV',
    'quantity_sold': 1,
    'total_price': 1600000.00
},
{
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': 'Paul Ryan',
    'sold_item': 'Radio',
    'quantity_sold': 1,
    'total_price': 60000.00
},
{
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': 'Jane Logan',
    'sold_item': 'Sugar',
    'quantity_sold': 4,
    'total_price': 50000.00
}
]

class Sale:
    def __init__(self, sales_person, sold_item, quantity_sold, total_price, id = str(uuid.uuid4())):
        self.sales_person = sales_person
        self.sold_item = sold_item
        self.quantity_sold = quantity_sold
        self.total_price = total_price
        self.id = id
    def get_sales(self):
        return sales
