class Product:
    in_stock = False
    def __init__(self, category='', name = '', quantity=0, price=0.00):
        self.category = category
        self.quantity = quantity
        self.price = price
        self.name = name