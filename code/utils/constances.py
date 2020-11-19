import cv2

ALL_STATES = ['checkout', 'dairy', 'drinks', 'fruit', 'spices']

STATE_LOCATION = {
  'dairy': [3, 4],
  'drinks': [7,4],
  'fruit': [11, 4],
  'spices': [15, 4],
  'checkout': [3, 8],
  'entrance': [14, 11]
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
##..##..##..##...#
##...............#
##############GG##
""".strip()

TILES = cv2.imread("./graphics/tiles.png")