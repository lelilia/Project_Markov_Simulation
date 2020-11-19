#
from supermarket import Supermarket
from customer import Customer
import numpy as np

#
class CoronaSupermarket(Supermarket):

    def __init__(self, customer_limit = 5):
        '''
        constructor inheriting from class Supermarket
        '''
        super().__init__()
        self.customer_limit = customer_limit
        self.corona_queue = []

    def corona_stop(self):
        '''
        customer needs to wait in queue if already 5 customers are in the market.
        '''
        if len(self.customers) > self.customer_limit:
            self.corona_queue = self.customers[self.customer_limit:]
            self.customers = self.customers[:self.customer_limit]

    def corona_go(self):
        '''
        next customer is allowed to enter the market if less than 5 customers are already in the market.
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

