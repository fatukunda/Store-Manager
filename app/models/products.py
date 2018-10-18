import uuid

class Product:
    def __init__(self, name, category, quantity, price, id= str (uuid.uuid4())):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.id = id

"""Dummy products list"""
products = [
{
    'id': str(uuid.uuid4()),
    'name': 'Samsung 32 inch Tv',
    'category': 'Electronics', 
    'quantity': 10,
    'price': 16000000
},
{
    'id': str(uuid.uuid4()),
    'name': 'Samsung 24 inch Tv',
    'category': 'Electronics', 
    'quantity': 5,
    'price': 12000000
},
{
    'id': str(uuid.uuid4()),
    'name': 'Dell laptop',
    'category': 'Computers', 
    'quantity': 7,
    'price': 2500000
},
]
