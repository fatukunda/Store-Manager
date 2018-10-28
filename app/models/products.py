import uuid

class Product:
    name = ''
    in_stock = False
    def __init__(self, category='', quantity=0, price=0.00, id= str (uuid.uuid4())):
        self.category = category
        self.quantity = quantity
        self.price = price
        self.id = id
