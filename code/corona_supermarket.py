#
from supermarket import Supermarket
from customer import Customer
import numpy as np

#
class CoronaSupermarket(Supermarket):
    '''
    inherits from parent class Supermarket and simulates a supermarket during Corona restrictions.
    '''

    def __init__(self, customer_limit = 5):
        '''
        constructor inheriting from class Supermarket
        and defines how much customers are allowed to enter the market at the same time 
        '''
        super().__init__(corona=True)
        self.customer_limit = customer_limit
        self.corona_queue = []

    def corona_stop(self):
        '''
        customer needs to wait in queue if limit of customers in the supermarket has already been reached.
        '''
        if len(self.customers) > self.customer_limit:
            self.corona_queue = self.customers[self.customer_limit:]
            self.customers = self.customers[:self.customer_limit]

    def corona_go(self):
        '''
        next customer is allowed to enter the market if customer number in the supermarket is <= defined limit.
        '''
        if not self.customers:
            pass
        elif self.corona_queue:
            customer_len = len(self.customers)
            new_customers = self.customer_limit - customer_len
            for _ in range(new_customers):
                if self.corona_queue:
                    self.customers.append(self.corona_queue[0])
                    self.corona_queue.pop(0)

