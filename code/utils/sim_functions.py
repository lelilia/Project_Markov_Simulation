
from constances import TILE_SIZE


def get_tile_parameters(y, x):
  '''
  returns the pixels for a tile
  in order to make it easier it first takes the y and than the x so one can count the tiles in the more comfortable way x,y
  '''
  return [x * TILE_SIZE : (x + 1) * TILE_SIZE, y * TILE_SIZE : (y + 1) * TILE_SIZE]

