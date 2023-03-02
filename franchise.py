from order_factory import OrderFactory
from logger import logger

class Franchise:
    def __init__(self, location_number:int):
        self.location_number = location_number
    
    def place_order(self):
        order = input("""Welcome to 3 Dishes Restaurant. What would you like to order?
        Please enter an order of Pasta 🍝, Pizza 🍕, or Salad 🥗: 
        \n""")
        orders = OrderFactory.create_order(order)
        logger.log_transaction(orders, self.location_number)