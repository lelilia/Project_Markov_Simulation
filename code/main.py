import numpy as np
import cv2
import time
from random import random

# local import
from tiles import SupermarketMap
from supermarket import Supermarket
from customer import Customer
from utils.constances import MARKET, TILES, OFS
from utils.functions import get_transition_matrix, get_supermarket_data

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

    go_to_next_minute(market, supermarket, frame)
    cv2.imshow("frame", frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
      break
  cv2.destroyAllWindows()
  market.write_image("./graphics/supermarket.png")

if __name__ == "__main__":
  simulate_n_customers(5)
    