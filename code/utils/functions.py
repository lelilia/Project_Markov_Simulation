import pandas as pd
import numpy as np


def get_the_original_data(list_of_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']):
  '''
  read in the original data for all weekdays and return a dataframe with all the days and added a value to the customer_no to distinguish between days
  Parameters
  ----------
  list_of_days: list of strings
  all the days that should be concatenated into the dataframe

  Return
  ------
  df: pandas DataFrame with timestamp, customer_no, location
  '''
  for i, day in enumerate(list_of_days):
    day_df = pd.read_csv(f'../data/{day}.csv', sep = ';', index_col = 'timestamp', parse_dates = True)
    if i == 0:
      df = day_df
      continue
    day_df.customer_no = day_df.customer_no + i * 10_000
    df = pd.concat([df, day_df])

  return df

def get_column_next_aisle(df):
  '''
  calculate the next aisle a customers goes to if it does not exist already

  Parameters
  ----------
  df: DataFrame

  Returns
  -------
  df: DataFrame with next_aisle column
  '''
  if 'next_aisle' in df.columns:
    return df
  df['next_aisle'] = df.groupby('customer_no').location.shift(-1)
  return df

def get_transition_matrix(df):
  '''
  calculates the transition matrix for a dataframe

  Parameters
  ----------
  df : Pandas DataFrame
  Data Frame with the following columns:
    - timestamp: DateTime
    - customer_no: Integer
    - location: String

  Return
  ------
  transition_matrix: Pandas DataFrame
  '''
  # add new column for the next aisle
  df = get_column_next_aisle(df)

  # calculate transition_matrix via crosstab, normalized on the rows
  transition_matrix = pd.crosstab(df['location'], df['next_aisle'], normalize=0)

  return transition_matrix

def save_compounded_dataframe():
  '''
  Saves the original data in a concatinated dataframe once
  '''
  supermarket = get_the_original_data()
  supermarket = backfill_data(supermarket)
  supermarket.to_csv('../data/supermarket.csv')

def get_supermarket_data():
  '''
  get the supermarket dataframe from csv
  '''
  supermarket = pd.read_csv('../data/supermarket.csv', index_col = 'timestamp', parse_dates = True)
  return supermarket

def backfill_data(df):
  '''
  fills in the dataFrame with positions for the customers for each minute they are in the store
  '''
  df = df.groupby('customer_no').resample('60S').bfill()
  df.drop('customer_no', axis = 1, inplace = True)
  df = df.reset_index().set_index('timestamp')
  df = df.sort_index()
  return df

