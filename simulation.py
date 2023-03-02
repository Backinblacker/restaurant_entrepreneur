from franchise import Franchise
class Simulation:
    def run_simulation(self):
        store_number1 = Franchise(1)
        store_number2 = Franchise(2)
        store_number3 = Franchise(3)
        
        store_number1.place_order()
        store_number3.place_order()
        store_number2.place_order()
        store_number3.place_order()
        store_number1.place_order()
        store_number2.place_order()