
import numpy as np
import cv2


TILE_SIZE = 32
OFS = 50

MARKET = """
##################
##..............##
##..##..##..#O..##
##..##..##..#O..##
##..##..##..#O..##
##..##..##..#u..##
##..##..##..#u..##
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tile   : a numpy array containing the tile image
        """
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split('\n')]
        self.xsize =  len(self.contents[0])
        self.ysize = len(self.contents)
        self.image = np.zeros((self.ysize * TILE_SIZE, self.xsize * TILE_SIZE, 3), dtype=np.uint8)
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        # empty shelf
        if char == '#':
            return self.tiles[0 : TILE_SIZE, 2*TILE_SIZE : 3 * TILE_SIZE]
        # gate
        elif char == 'G':
            return self.tiles[7 * TILE_SIZE : 8 * TILE_SIZE, 3 * TILE_SIZE : 4 * TILE_SIZE]
        # cash register
        elif char == 'C':
            return self.tiles[1 * TILE_SIZE : 2 * TILE_SIZE, 8 * TILE_SIZE : 9 * TILE_SIZE]
        # eggplant
        elif char == 'O':
            return self.tiles[1 * TILE_SIZE: 2 * TILE_SIZE, 11 * TILE_SIZE : 12 * TILE_SIZE]
        # pink umbrella
        elif char == 'u':
            return self.tiles[2 * TILE_SIZE: 3 * TILE_SIZE, 9 * TILE_SIZE : 10 * TILE_SIZE]
        else:
            return self.tiles[TILE_SIZE : 2 * TILE_SIZE, 2 * TILE_SIZE : 3 * TILE_SIZE]

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[y * TILE_SIZE:(y+1)*TILE_SIZE,
                      x * TILE_SIZE:(x+1)*TILE_SIZE] = bm

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[OFS:OFS+self.image.shape[0], OFS:OFS+self.image.shape[1]] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


background = np.zeros((700, 1000, 3), np.uint8)
tiles = cv2.imread('./graphics/tiles.png')

market = SupermarketMap(MARKET, tiles)

while True:
    frame = background.copy()
    market.draw(frame)

    cv2.imshow('frame', frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

cv2.destroyAllWindows()

market.write_image("./graphics/supermarket.png")
