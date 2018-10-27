import uuid

class Product:
    in_stock= False
    quantity_in_stock = 0

    def __init__(self, name='', category='', price=0.00, id=str(uuid.uuid4())):
        self.name = name
        self.category=category
        self.price=price,
        self.id=id