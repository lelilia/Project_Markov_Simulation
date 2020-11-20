''' customer class for the supermarket simulation'''

import numpy as np
from random import sample

# local imports
from utils.constances import ALL_STATES, TILES, TILE_SIZE, STATE_LOCATION, OFS, GRID, POSSIBLE_MOVES
from utils.a_star import find_path


class Customer:

    '''
    a single customer that moves through the supermarket in a MCMC simulation
    '''

    def __init__(self, customer_id, state, transition_mat, terrain_map, ghost=3):
        '''initiate'''
        self.id = customer_id
        self.state = state
        self.transition_mat = transition_mat
        self.history = []
        print(ghost)
        # visualization
        self.terrain_map = terrain_map
        self.image = TILES[8 * TILE_SIZE: 9 * TILE_SIZE,
                           ghost * TILE_SIZE: (ghost + 1) * TILE_SIZE]
        location = sample(STATE_LOCATION[self.state],1)[0]
        self.x = location[0]
        self.y = location[1]
        #self.x = STATE_LOCATION[self.state][0]
        #self.y = STATE_LOCATION[self.state][1]
        self.path = []

    def __repr__(self):
        '''
        define the print return
        '''
        return f'<Customer {self.id} in {self.state} at {self.x} {self.y}>'

    def is_active(self):
        '''
        Returns True if the customer has not reached the checkout for the second time yet.
        False otherwise.
        '''
        if self.history.count('checkout') > 1:
            return False
        return True

    def is_moving(self):
        '''
        Returns True if the customer still has to move to the destination.
        '''
        if len(self.path) > 0:
            return True
        return False

    def next_state(self):
        '''
        Propagates the customer to the next state using a weighted random choice from the
        transition probabilities conditional on the current state.
        Returns nothing.
        '''
        start_location = tuple([self.x, self.y][::-1])
        #start_state = tuple(STATE_LOCATION[self.state][::-1])
        self.history.append(self.state)
        next_aisle = np.random.choice(ALL_STATES, p = self.transition_mat.loc[self.state])
        next_location = tuple(sample(STATE_LOCATION[next_aisle],1)[0][::-1])
        self.state = next_aisle
        #finish_state = tuple(STATE_LOCATION[self.state][::-1])

        if start_location != next_location:

            self.path = find_path(
                GRID, start_location, next_location, POSSIBLE_MOVES)[::-1]


    def move(self):
        '''
        Move the customer on the path between two aisles
        '''
        if len(self.path) > 0:
            new_y, new_x = self.path.pop()
            self.x = new_x
            self.y = new_y

    def draw(self, frame):
        '''
        Draw customer on the visualization
        '''
        x_pos = OFS + self.x * TILE_SIZE
        y_pos = OFS + self.y * TILE_SIZE
        frame[y_pos: y_pos + TILE_SIZE, x_pos: x_pos + TILE_SIZE] = self.image
