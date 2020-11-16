'''
Takes the data from the weekdays and saves it in a file called supermarket
It adds a number to the customerID so they are distinguishable from each other on different days
'''

import pandas as pd
import matplotlib.pyplot as plt

monday =    pd.read_csv('../data/monday.csv',    sep = ';', index_col = 'timestamp')
tuesday =   pd.read_csv('../data/tuesday.csv',   sep = ';', index_col = 'timestamp')
wednesday = pd.read_csv('../data/wednesday.csv', sep = ';', index_col = 'timestamp')
thursday =  pd.read_csv('../data/thursday.csv',  sep = ';', index_col = 'timestamp')
friday =    pd.read_csv('../data/friday.csv',    sep = ';', index_col = 'timestamp')

# add the number for the day
monday.customer_no    = monday.customer_no    + 10_000
tuesday.customer_no   = tuesday.customer_no   + 20_000
wednesday.customer_no = wednesday.customer_no + 30_000
thursday.customer_no  = thursday.customer_no  + 40_000
friday.customer_no    = friday.customer_no    + 50_000

# concat all days to one dataframe
supermarket = pd.concat([monday, tuesday, wednesday, thursday, friday])

# save the dataframe to a csv file
supermarket.to_csv('../data/supermarket.csv')