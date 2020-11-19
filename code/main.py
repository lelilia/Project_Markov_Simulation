from supermarket import Supermarket
from corona_supermarket import CoronaSupermarket
from utils.functions import *

#supermarket = Supermarket()
corona_supermarket = CoronaSupermarket(customer_limit=5)

"""
corona_supermarket.add_new_customers()
corona_supermarket.corona_stop()
corona_supermarket.next_minute()
corona_supermarket.print_customers()
"""



corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()
corona_supermarket.add_new_customers()



while len(corona_supermarket.customers) > 0:
  corona_supermarket.corona_stop()
  corona_supermarket.next_minute()
  corona_supermarket.print_customers()
  corona_supermarket.get_time()
  corona_supermarket.remove_existing_customers()
  corona_supermarket.corona_go()


