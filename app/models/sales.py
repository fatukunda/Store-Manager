import uuid
from time import ctime
from app.models.attendant import Attendant


class Sale:
    sales_person =''
    sold_item = ''
    quantity_sold = 0
    total_price = 0.00
    unit_price = 0.00

    def __init__(self, id = str(uuid.uuid4()), date =ctime()):
       
        self.id = id
        self.date = date

# Create dummy attendants data
# Attendant1
attendant1 = Attendant('simonLee', 'user')
attendant1.email = 'lee@store.com'
attendant1.first_name = 'Simon'
attendant1.last_name = 'Lee'
# Attendant 2
attendant2 = Attendant('pRyan', 'user')
attendant2.email = 'ryan@store.com'
attendant2.first_name = 'Paul'
attendant2.last_name = 'Ryan'
# Attendant 3
attendant3 = Attendant('jLogan', 'user')
attendant3.email = 'logan@store.com'
attendant3.first_name = 'Jane'
attendant3.last_name = 'Logan'
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
