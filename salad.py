from order import Order

class Salad (Order):
    def __init__(self):
        super().__init__("Dinner Salad", 11)