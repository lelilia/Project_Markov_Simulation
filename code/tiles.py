''' SupermarketMap class of the supermarket simulation project'''

import numpy as np
import cv2


from utils.constances import TILE_SIZE, OFS


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tile   : a numpy array containing the tile image
        """
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split("\n")]
        self.xsize = len(self.contents[0])
        self.ysize = len(self.contents)
        self.image = np.zeros(
            (self.ysize * TILE_SIZE, self.xsize * TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def get_tile_parameters(self, y, x):
        '''
        returns the pixels for a tile
        in order to make it easier it first takes the y and than the x so one can count
        the tiles in the more comfortable way x,y
        '''
        return self.tiles[x * TILE_SIZE: (x + 1) * TILE_SIZE, y * TILE_SIZE: (y + 1) * TILE_SIZE]

    def get_tile(self, char):
        """returns the array for a given tile character"""
        # empty shelf
        if char == '#':
            return self.get_tile_parameters(0, 0)
        # gate
        elif char == 'G':
            return self.get_tile_parameters(3, 7)
        # cash register
        elif char == 'C':
            return self.get_tile_parameters(8, 1)
        # eggplant
        elif char == 'O':
            return self.get_tile_parameters(11, 1)
        # grapes
        elif char == 't':
            return self.get_tile_parameters(4, 4)
        # strawberry
        elif char == 's':
            return self.get_tile_parameters(5, 1)
        # tomato
        elif char == 'T':
            return self.get_tile_parameters(5, 3)
        # pink umbrella
        elif char == 'u':
            return self.get_tile_parameters(9, 2)
        # vase
        elif char == 'v':
            return self.get_tile_parameters(10, 0)
        # candy 1
        elif char == 'b':
            return self.get_tile_parameters(3, 0)
        # candy 2
        elif char == 'c':
            return self.get_tile_parameters(3, 1)
        # cashier
        elif char == 'g':
            return self.get_tile_parameters(3, 8)
        # empty shelve
        elif char == 'e':
            return self.get_tile_parameters(9, 8)
        # toiletpaper
        elif char == 'k':
            return self.get_tile_parameters(8, 8)

        else:
            return self.get_tile_parameters(2, 1)

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[
                    y * TILE_SIZE: (y + 1) * TILE_SIZE,
                    x * TILE_SIZE: (x + 1) * TILE_SIZE,
                ] = bm

    def draw(self, frame):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[
            OFS: OFS + self.image.shape[0], OFS: OFS + self.image.shape[1]
        ] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


