'''
estimate the total revenue for a customer using the following table
section   revenue per minute
fruit     4€
spices    3€
dairy     5€
drinks    6€
'''

# third party imports
import pandas as pd
import numpy as np
import sys

# local application imports
from utils.functions import get_concatinated_data

supermarket = get_concatinated_data()
print(supermarket)