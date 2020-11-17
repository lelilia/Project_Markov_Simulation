import numpy as np

class Customer:
  '''
  a single customer that moves through the supermarket in a MCMC simulation
  '''
  def __init__(self, id, state, transition_mat):
    '''initiate'''
    self.id = id
    self.state = state
    self.transition_mat = transition_mat
    self.history = []

  def __repr__(self):
    '''define the print return'''
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
    self.state = np.random.choice(['spices', 'drinks', 'fruit'])
    #TODO
