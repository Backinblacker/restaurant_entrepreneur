class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0
    
    def log_transaction (self, order, store_number):
        self.daily_sales += order.price
        self.transaction_count +=1
        file = open("log.txt", "a")
        file.write(f"Transaction #{self.transaction_count}: {order.dish_name} at Store Number {store_number}: ${order.price}. Total: ${self.daily_sales}\n")
        file.close()
        
logger = Logger()
