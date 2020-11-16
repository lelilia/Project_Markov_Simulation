import pandas as pd

supermarket = pd.read_csv('../data/supermarket.csv', index_col='timestamp')
supermarket['last_aisle'] = supermarket.groupby('customer_no').location.shift(-1)



prob = pd.crosstab(supermarket['last_aisle'], supermarket['location'], normalize=0)
# 0, 1, index, columns, all

#print(supermarket.head())
#print(supermarket.tail(50))
print(prob)
print(prob.sum(axis=1))

supermarket.to_csv('../data/sm-last_isle.csv')