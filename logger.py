class Logger:
    def __init__(self):
        self.transaction_count = 1
        self.daily_sales = 0
    
    def log_transaction (order, location_number):
        pass
        

# a is append w is overwrite and r is readme
# file = open("log.txt", "r")

# What information goes into the message
# This will only append it to the end of the line so need to use \n
# file.write("")

# Wrtie the message and then close it
# file.close()

# Output will look like
    # Transaction #1 : Order at Location X - $15 Total: $15
    # Transaction #2 : Order at Location X - $15 Total: $30
    # Transaction #3 : Order at Location X - $15 Total: $45