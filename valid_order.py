# Works but breaks franchise, order_factory, logger
class ValidOrder:
    @staticmethod
    def order_validation():
        user_input = False
        while user_input == False:
            input = input("""Welcome to 3 Dishes Restaurant. What would you like to order?
            Please enter an order of Pasta 🍝, Pizza 🍕, or Salad 🥗: 
            \n""")
            dishes = ["Pizza", "pizza", "Pasta", "pasta", "Salad", "salad"]
            if input == dishes:
                user_input = True
                return input
            else:
                print("This is not a valid order. Please order something else.")
