# third party import
import numpy as np
import pandas as pd

# local import
from customer import Customer


class Supermarket:
  '''
  manages multiple Customer instances that are currently in the market.
  '''

  def __init__(self):
    # a list of Customer objects
    self.customers = []
    self.minutes = 0
    self.last_id = 0

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
    print(f'There are {len(self.customers)} in the supermarket at the moment.\n')

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
    customer = Customer(7, 'dairy', [0, 1])
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
