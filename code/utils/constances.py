import cv2

ALL_STATES = ['checkout', 'dairy', 'drinks', 'fruit', 'spices']

STATE_LOCATION = {
  'dairy':    [4,  3],
  'drinks':   [4,  7],
  'fruit':    [4, 11],
  'spices':   [4, 15],
  'checkout': [8,  3],
  'entrance': [11, 14]
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