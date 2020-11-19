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

def go_to_next_minute(supermarket, frame, adding_prob = 0):
  '''
  simulate next minute
  '''
  if random() < adding_prob:
    supermarket.add_new_customers()
  supermarket.remove_exitsting_customers()
  supermarket.print_customers()
  supermarket.draw_customers(frame)
  supermarket.next_minute()
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

  while len(supermarket.customers) > 0:
    time.sleep(1)
    frame = background.copy()
    market.draw(frame)
    go_to_next_minute(supermarket, frame)
    cv2.imshow("frame", frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
      break
  cv2.destroyAllWindows()
  market.write_image("./graphics/supermarket.png")

if __name__ == "__main__":
  simulate_n_customers(5)
    # background = np.zeros((700, 1000, 3), np.uint8)

    # market = SupermarketMap(MARKET, TILES)

    # # instantiate a customer
    # supermarket = Supermarket(market)
    # supermarket.add_new_customers()
    # supermarket.add_new_customers()

    # while True:
    #     time.sleep(1)
    #     frame = background.copy()
    #     market.draw(frame)
    #     for customer in supermarket.customers:
    #       customer.draw(frame)
    #     supermarket.next_minute()
    #     supermarket.print_customers()
    #     cv2.imshow("frame", frame)

    #     key = chr(cv2.waitKey(1) & 0xFF)
    #     # if key == 'w':
    #     #     customer.move('up')
    #     # elif key == 'a':
    #     #     customer.move('left')
    #     # elif key == 'd':
    #     #     customer.move('right')
    #     # elif key == 's':
    #     #     customer.move('down')

    #     if key == "q":
    #         break

    # cv2.destroyAllWindows()

    # market.write_image("./graphics/supermarket.png")
