import pandas as pd
import numpy as np

supermarket = pd.read_csv('../data/supermarket.csv', index_col = 'timestamp')
# print(supermarket)

# add the next_isle
supermarket['next_isle'] = supermarket.groupby('customer_no').location.shift(-1)
# print(supermarket.tail(50))

print(supermarket[supermarket.customer_no == 51496])

supermarket2 = pd.read_csv('../data/supermarket.csv', index_col = 'timestamp')
print(supermarket2[supermarket2.customer_no == 51496])

# pd.crosstab(df['weather'], df['day_after'])

probability = pd.crosstab(supermarket['location'], supermarket['next_isle'], normalize=0)
print(probability)