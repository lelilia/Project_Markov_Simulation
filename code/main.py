import numpy as np
import cv2
import time
from random import random

# local import
from tiles import SupermarketMap
from supermarket import Supermarket
from customer import Customer
from utils.constances import MARKET, TILES, OFS, GRID, POSSIBLE_MOVES, STATE_LOCATION, TRANSITION_MATRIX
from utils.functions import get_transition_matrix, get_supermarket_data, get_first_aisle_probability
from utils.a_star import find_path

def go_to_next_minute(market, supermarket, frame, adding_prob = 0):
  '''
  simulate next minute
  '''
  market.draw(frame)
  if random() < adding_prob:
    supermarket.add_new_customers()
  supermarket.remove_exitsting_customers()
  supermarket.print_customers()

  supermarket.draw_customers(frame)
  supermarket.next_minute()
  time.sleep(1)
  return supermarket

def move_between_minutes(market, supermarket, frame):
    market.draw(frame)
    supermarket.remove_exitsting_customers()
    supermarket.move_customers()
    supermarket.print_customers()
    supermarket.draw_customers(frame)
    time.sleep(0.1)
def simulate_n_customers(n):
  '''
  Simulate n customers that start together in the store.
  No new customers are added over time.
  The simulation ends once all are checked out.
  '''
  background = np.zeros((700, 1000, 3), np.uint8)
  market = SupermarketMap(MARKET, TILES)
  supermarket = Supermarket(market)
  for _ in range(n):
    supermarket.add_new_customers()
  frame = background.copy()

  while len(supermarket.customers) > 0:
    if supermarket.customers_to_move:
      move_between_minutes(market, supermarket, frame)
    else:
      go_to_next_minute(market, supermarket, frame)
    cv2.imshow("frame", frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
      break
  cv2.destroyAllWindows()
  market.write_image("./graphics/supermarket.png")

def go_to_next_minute_without_simulation(supermarket, adding_prob = 0):
  '''
  simulate next minute
  '''
  if random() < adding_prob:
    supermarket.add_new_customers()
  supermarket.remove_exitsting_customers()
  supermarket.print_customers()
  while supermarket.customers_to_move:
    supermarket.remove_exitsting_customers()
    supermarket.move_customers()
    supermarket.print_customers()
    time.sleep(1)
  supermarket.next_minute()
  return supermarket

def simulate_n_customers_without_simulation(n):
  '''
  Simulate n customers that start together in the store.
  No new customers are added over time.
  The simulation ends once all are checked out.
  '''
  supermarket = Supermarket()
  for _ in range(n):
    supermarket.add_new_customers()

  while len(supermarket.customers) > 0:
    go_to_next_minute_without_simulation(supermarket)

  # supermarket.save_dataframe()

if __name__ == "__main__":
  # print(TRANSITION_MATRIX)

  simulate_n_customers(15)
  # start = STATE_LOCATION['checkout']
  # print(find_path(GRID, start, (4,3), POSSIBLE_MOVES))
  # start = tuple(STATE_LOCATION['drinks'][::-1])
  # print(start)
  # end = tuple(STATE_LOCATION['checkout'][::-1])
  # print(end)
  # print(find_path(GRID, start, end, POSSIBLE_MOVES))