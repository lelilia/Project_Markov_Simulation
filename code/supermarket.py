''' supermarket class for the supermarket simulation '''

# third party import
import numpy as np


# local import
from customer import Customer
from utils.functions import get_transition_matrix, get_supermarket_data, get_first_aisle_probability



class Supermarket:
    '''
    manages multiple Customer instances that are currently in the market.
    '''

    # class variables
    shelves = ['dairy', 'drinks', 'fruit', 'spices']

    def __init__(self, corona = False, market=0):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.transition_matrix = get_transition_matrix(get_supermarket_data())
        self.first_aisle = get_first_aisle_probability()
        # self.dataframe = pd.DataFrame(columns=['timestamp', 'customer_no', 'location'])
        self.terrain_map = market
        self.customers_to_move = False
        self.corona = corona

    def __repr__(self):
        pass

    def get_time(self):
        '''
        print current time in HH:MM format
        '''
        hour = self.minutes // 60 + 7
        minutes = self.minutes % 60
        return f'{str(hour).zfill(2)}:{str(minutes).zfill(2)}'

    def print_customers(self):
        '''
        print all customers with the current time and id in CSV format.
        '''
        current_time = self.get_time()
        print(f'{current_time}: There are {len(self.customers)} customer(s) in the supermarket at the moment.\n')

        for customer in self.customers:
            print(customer)
            # self.dataframe.append([current_time, customer.id, customer.state])
        print()

    def draw_customers(self, frame):
        '''
        draw all the customers
        '''
        for customer in self.customers:
            customer.draw(frame)

    def next_minute(self):
        '''
        propagates all customers to the next state.
        '''
        self.minutes += 1
        for customer in self.customers:
            customer.next_state()
        self.customers_to_move = True

    def move_customers(self):
        '''
        move customers on their path between aisles
        '''
        for customer in self.customers:
            customer.move()

    def add_new_customers(self):
        '''
        randomly creates new customers.
        '''
        customer_id = self.last_id
        self.last_id += 1
        print(self.corona)
        if self.corona:
          ghost = np.random.choice([2,3,4,5,6,7])
        else:
          ghost = np.random.choice([1, 2])
        location = np.random.choice(self.shelves, p=self.first_aisle)
        customer = Customer(
            customer_id, location, self.transition_matrix, self.terrain_map, ghost)
        self.customers.append(customer)

    def remove_exitsting_customers(self):
        '''
        removes every customer that is not active any more.
        '''
        self.customers_to_move = False
        for customer in self.customers:
            if not customer.is_active():
                self.customers.remove(customer)
            if customer.is_moving():
                self.customers_to_move = True
        print(self.customers_to_move)
