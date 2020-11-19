import numpy as np

# local imports
from tiles import SupermarketMap
from utils.constances import ALL_STATES, TILES, TILE_SIZE, STATE_LOCATION

class Customer:
  '''
  a single customer that moves through the supermarket in a MCMC simulation
  '''
  def __init__(self, id, state, transition_mat, terrain_map):
    '''initiate'''
    self.id = id
    self.state = state
    self.transition_mat = transition_mat
    self.history = []

    # visualization
    self.terrain_map = terrain_map
    self.image = TILES[7 * TILE_SIZE : 8 * TILE_SIZE, : TILE_SIZE]
    self.x = STATE_LOCATION[self.state][1] * TILE_SIZE
    self.y = STATE_LOCATION[self.state][0] * TILE_SIZE

  def __repr__(self):
    '''
    define the print return
    '''
    return f'<Customer {self.id} in {self.state}>'

  def is_active(self):
    '''
    Returns True if the customer has not reached the checkout for the second time yet, False otherwise.
    '''
    if self.history.count('checkout') > 1:
      return False
    return True

  def next_state(self):
    '''
    Propagates the customer to the next state using a weighted random choice from the transition probabilities conditional on the current state.
    Returns nothing.
    '''
    self.history.append(self.state)
    self.state = np.random.choice(ALL_STATES, p = self.transition_mat.loc[self.state])

  def draw(self, frame):
    x_pos = OFS + self.x * TILE_SIZE
    y_pos = OFS + self.y * TILE_SIZE
    frame[y_pos : y_pos + TILE_SIZE, x_pos : x_pos + TILE_SIZE] = self.image

