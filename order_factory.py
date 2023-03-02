from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory():
    @staticmethod
    def create_order(input):
        if input == "Pasta" or input == "pasta":
            return Pasta()
        elif input == "Pizza" or input == "pizza":
            return Pizza()
        elif input == "Salad" or input == "salad":
            return Salad()
        else:
            print("This is not a valid input.")    

# Attempting to handle bad user_input

# from valid_order import ValidOrder

# class OrderFactory():
#     @staticmethod
#     def create_order():
#         dishes = [Pizza(), Pasta(), Salad()]
#         order = ValidOrder.order_validation(dishes)
#         return dishes