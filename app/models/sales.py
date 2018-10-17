import uuid
from time import ctime
from app.models.attendant import Attendant


class Sale:
    def __init__(self, sales_person = '', sold_item='', quantity_sold= 0, total_price=0.00,unit_price=0.00, id = str(uuid.uuid4()), date =ctime()):
        self.sales_person = sales_person
        self.sold_item = sold_item
        self.quantity_sold = quantity_sold
        self.total_price = total_price
        self.id = id
        self.unit_price = unit_price
        self.date = date

# Create dummy attendants data
# Attendants
attendant1 = Attendant('Simon', 'Lee', 'lee@store.com', 'simonLee', 'user')
attendant2 = Attendant('Paul', 'Ryan', 'ryan@store.com', 'pRyan', 'user')
attendant3 = Attendant('Jane', 'Logan', 'logan@store.com', 'jLogan', 'user')

# Create dummy sales data
sales = [
    {
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': attendant1.username,
    'sold_item': 'Samsung 32 inch TV',
    'quantity_sold': 1,
    'unit_price': 1600000.00,
    'total_price': 1600000.00
    },
    {
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': attendant1.username,
    'sold_item': 'Radio',
    'unit_price': 60000.00,
    'quantity_sold': 2,
    'total_price': 120000.00
    },
    {
    'id': str(uuid.uuid4()),
    'date': ctime(),
    'sales_person': attendant3.username,
    'sold_item': 'Sugar',
    'unit_price': 10000.00,
    'quantity_sold': 4,
    'total_price': 50000.00
    }
]
