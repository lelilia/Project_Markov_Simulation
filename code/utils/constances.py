import cv2
import numpy as np
import pandas as pd


ALL_STATES = ['checkout', 'dairy', 'drinks', 'fruit', 'spices']#, 'entry', 'exit']

STATE_LOCATION = {
  'dairy':    [3,  4],
  'drinks':   [7,  4],
  'fruit':    [11, 4],
  'spices':   [15, 4],
  'checkout': [3,  8],
  'entry': [14, 11],
  'exit': [15,11]
}

TILE_SIZE = 32
OFS = 50

MARKET = """
##################
##..............##
#c..bs..tO..Tv..u#
#b..ct..sT..Ou..v#
#c..bs..tO..Tv..u#
#b..ct..sT..Ou..v#
#c..bs..tO..Tv..u#
##...............#
##..C#..C#..C#...#
##..#g..##..##...#
##...............#
##############GG##
""".strip()

TILES = cv2.imread("./graphics/tiles.png")

# grid for the a* algorithm
GRID = np.array([
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]])

# possible moves for the a* algorithm
POSSIBLE_MOVES = [(0,1), (0,-1), (1, 0), (-1,0)]

TRANSITION_MATRIX = pd.read_csv('../data/transition_matrix.csv', index_col=0)