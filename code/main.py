from supermarket import Supermarket
from utils.functions import *

supermarket = Supermarket()

supermarket.add_new_customers()
supermarket.add_new_customers()
supermarket.add_new_customers()


while len(supermarket.customers) > 0:
  supermarket.next_minute()
  supermarket.print_customers()
  supermarket.get_time()
  supermarket.remove_exitsting_customers()


