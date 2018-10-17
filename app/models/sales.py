import uuid
from time import ctime
from app.models.attendant import Attendant

# Create dummy attendants data
# Attendant 1
attendant1 = Attendant('Simon', 'Lee', 'lee@store.com', 'simonLee', 'user')
attendant2 = Attendant('Paul', 'Ryan', 'ryan@store.com', 'pRyan', 'user')
attendant3 = Attendant('Jane', 'Logan', 'logan@store.com', 'jLogan', 'user')
sales = [
    {
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': attendant1.username,
    'sold_item': 'Samsung 32 inch TV',
    'quantity_sold': 1,
    'total_price': 1600000.00
},
{
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': attendant1.username,
    'sold_item': 'Radio',
    'quantity_sold': 1,
    'total_price': 60000.00
},
{
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': attendant3.username,
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
