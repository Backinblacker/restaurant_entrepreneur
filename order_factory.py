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