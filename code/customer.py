import numpy as np

# local imports
from tiles import SupermarketMap
from utils.constances import ALL_STATES, TILES, TILE_SIZE, STATE_LOCATION, OFS

class Customer:
  '''
  a single customer that moves through the supermarket in a MCMC simulation
  '''
  def __init__(self, id, state, transition_mat, terrain_map):
    '''initiate'''
    self.id =             id
    self.state =          state
    self.transition_mat = transition_mat
    self.history =        []

    # visualization
    self.terrain_map =  terrain_map
    self.image =        TILES[8 * TILE_SIZE : 9 * TILE_SIZE, 3 * TILE_SIZE: 4 *TILE_SIZE]
    self.x =            STATE_LOCATION[self.state][1]
    self.y =            STATE_LOCATION[self.state][0]

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
    self.x = STATE_LOCATION[self.state][1]
    self.y = STATE_LOCATION[self.state][0]

  # def move(self, direction):
  #   new_x = self.x
  #   new_y = self.y
  #   if direction == 'up':
  #       new_y -= 1
  #   elif direction == 'down':
  #       new_y += 1
  #   elif direction == 'left':
  #       new_x -= 1
  #   elif direction == 'right':
  #       new_x += 1

  #   if self.terrain_map.contents[new_y][new_x] == '.':
  #       self.x = new_x
  #       self.y = new_y

  def draw(self, frame):
    x_pos = OFS + self.x * TILE_SIZE
    y_pos = OFS + self.y * TILE_SIZE
    frame[y_pos : y_pos + TILE_SIZE, x_pos : x_pos + TILE_SIZE] = self.image

