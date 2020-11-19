# third party import
import numpy as np
import pandas as pd

# local import
from customer import Customer
from utils.functions import get_transition_matrix, get_supermarket_data, get_first_aisle_probability

class Supermarket:
  '''
  manages multiple Customer instances that are currently in the market.
  '''

  # class variables
  shelves = ['dairy', 'drinks', 'fruit', 'spices']

  def __init__(self, market):
    # a list of Customer objects
    self.customers = []
    self.minutes = 0
    self.last_id = 0
    self.transition_matrix = get_transition_matrix(get_supermarket_data())
    self.first_aisle = get_first_aisle_probability()
    # self.dataframe = pd.DataFrame(columns=['timestamp', 'customer_no', 'location'])
    self.terrain_map = market

  def __repr__(self):
    pass

  def get_time(self):
    '''
    print current time in HH:MM format
    '''
    hour = self.minutes // 60 + 7
    minutes = self.minutes % 60
    return f'{str(hour).zfill(2)}:{str(minutes).zfill(2)}'


  def print_customers(self):
    '''
    print all customers with the current time and id in CSV format.
    '''
    current_time = self.get_time()
    print(f'{current_time}: There are {len(self.customers)} customer(s) in the supermarket at the moment.\n')

    for customer in self.customers:
        print(customer)
        # self.dataframe.append([current_time, customer.id, customer.state])
    print()

  def draw_customers(self, frame):
    '''
    draw all the customers
    '''
    for customer in self.customers:
      customer.draw(frame)

  def save_dataframe(self, filename = '../data/simulation.csv'):
    '''
    Save the file to data
    '''
    # self.dataframe.to_csv(filename)
    pass

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
    id = self.last_id
    self.last_id += 1
    location = np.random.choice(self.shelves, p = self.first_aisle)
    customer = Customer(id, location, self.transition_matrix, self.terrain_map)
    self.customers.append(customer)

  def remove_exitsting_customers(self):
    '''
    removes every customer that is not active any more.
    '''
    for customer in self.customers:
      if not customer.is_active():
        self.customers.remove(customer)

