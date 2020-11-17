# third party import
import numpy as np
import pandas as pd

# local import
from customer import Customer
from utils.functions import get_transition_matrix, get_the_original_data

class Supermarket:
  '''
  manages multiple Customer instances that are currently in the market.
  '''

  def __init__(self):
    # a list of Customer objects
    self.customers = []
    self.minutes = 0
    self.last_id = 0
    self.data = get_the_original_data()
    self.transition_matrix = get_transition_matrix(self.data)
    self.customer_id = 0
  def __repr__(self):
    pass

  def get_time(self):
    '''
    current time in HH:MM format,
    '''
    hour = self.minutes // 60 + 7
    minutes = self.minutes % 60
    return f'{hour}:{minutes}'
    # TODO add zeros to make it two

  def print_customers(self):
    '''
    print all customers with the current time and id in CSV format.
    '''
    print(f'There are {len(self.customers)} customer(s) in the supermarket at the moment.\n')

    for customer in self.customers:
        print(customer)

  def next_minute(self):
    '''
    propagates all customers to the next state.
    '''
    self.minutes += 1
    for customer in self.customers:
      customer.next_state()

  def add_new_customers(self):
    '''
    randomly creates new customers.
    '''
    id = self.customer_id
    self.customer_id += 1
    location = np.random.choice(['dairy', 'drinks', 'fruit', 'spices'])
    customer = Customer(id, location, self.transition_matrix)
    self.customers.append(customer)

  def remove_exitsting_customers(self):
    '''
    removes every customer that is not active any more.
    '''
    for customer in self.customers:
      if not customer.is_active():
        self.customers.remove(customer)


test = Supermarket()
print(test.get_time())
test.print_customers()
test.add_new_customers()
test.print_customers()
test.next_minute()
test.print_customers()
print(test.get_time())
supermarket = get_the_original_data()
print(get_transition_matrix(supermarket))
test.add_new_customers()
test.add_new_customers()
test.print_customers()
test.next_minute()
test.print_customers()
