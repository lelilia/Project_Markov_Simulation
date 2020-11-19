import numpy as np

# local imports
from tiles import SupermarketMap
from utils.constances import ALL_STATES, TILES, TILE_SIZE, STATE_LOCATION, OFS, GRID, POSSIBLE_MOVES
from utils.a_star import find_path

class Customer:
  '''
  a single customer that moves through the supermarket in a MCMC simulation
  '''
  def __init__(self, id, state, transition_mat, terrain_map, ghost = 3):
    '''initiate'''
    self.id =             id
    self.state =          state
    self.transition_mat = transition_mat
    self.history =        []
    print(self.state)
    # visualization
    self.terrain_map =  terrain_map
    self.image =        TILES[8 * TILE_SIZE : 9 * TILE_SIZE, ghost * TILE_SIZE: (ghost + 1) *TILE_SIZE]
    self.x =            STATE_LOCATION[self.state][0]
    self.y =            STATE_LOCATION[self.state][1]
    self.path =         []


  def __repr__(self):
    '''
    define the print return
    '''
    return f'<Customer {self.id} in {self.state} at {self.x} {self.y}>'

  def is_active(self):
    '''
    Returns True if the customer has not reached the checkout for the second time yet, False otherwise.
    '''
    if self.history.count('checkout') > 1:
      return False
    return True

  def is_moving(self):
    if len(self.path) > 0:
      return True
    return False

  def next_state(self):
    '''
    Propagates the customer to the next state using a weighted random choice from the transition probabilities conditional on the current state.
    Returns nothing.
    '''
    start_state = tuple(STATE_LOCATION[self.state][::-1])
    self.history.append(self.state)
    self.state = np.random.choice(ALL_STATES, p = self.transition_mat.loc[self.state])
    print(self.state)
    finish_state = tuple(STATE_LOCATION[self.state][::-1])
    # self.x = STATE_LOCATION[self.state][0]
    # self.y = STATE_LOCATION[self.state][1]
    if start_state != finish_state:
      print('location switch')
      self.path = find_path(GRID, start_state, finish_state, POSSIBLE_MOVES )[::-1]
      print(self.path)

  def move(self):
    print('customer is moving')
    print(self.path)
    print(len(self.path))
    if len(self.path) > 0:
      print('in the if')
      new_y, new_x = self.path.pop()
      print(new_x, new_y)
      self.x = new_x
      self.y = new_y
    else:
      self.x = STATE_LOCATION[self.state][0]
      self.y = STATE_LOCATION[self.state][1]
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

