from customer import Customer
from utils.constances import *
from utils.functions import *

print(get_first_aisle_probability())
print(get_transition_matrix(get_supermarket_data()))
c = Customer(1, 'dairy', get_transition_matrix(get_supermarket_data()))

print(c)
c.move()
print(c)
c.next_state()
print(c)

