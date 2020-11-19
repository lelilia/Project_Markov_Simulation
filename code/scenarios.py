from random import random
from supermarket import Supermarket

def go_to_next_minute(supermarket, adding_prob = 1):
  '''
  simulate next minute
  '''
  if random() > adding_prob:
    supermarket.add_new_customers()
  supermarket.get_time()
  supermarket.remove_exitsting_customers()
  supermarket.print_customers()
  supermarket.next_minute()
  return supermarket

def simulate_normal_day(prob_of_new_customer = 0.6):
  '''
  simulate a normal day in the supermarket
  '''
  supermarket = Supermarket()

  # from 7 - 21 in minutes
  closing_time = (21 - 7) * 60

  while supermarket.minutes < closing_time:
    go_to_next_minute(supermarket, prob_of_new_customer)


def simulate_n_customers(n):
  '''
  Simulate n customers that start together in the store.
  No new customers are added over time.
  The simulation ends once all are checked out.
  '''
  supermarket = Supermarket()
  for _ in range(n):
    supermarket.add_new_customers()

  while len(supermarket.customers) > 0:
    go_to_next_minute(supermarket)


