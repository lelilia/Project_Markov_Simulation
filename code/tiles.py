import numpy as np
import cv2
import time

TILE_SIZE = 32
OFS = 50

MARKET = """
##################
##..............##
##..b#..##..#O..##
##..c#..##..#O..##
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
        in order to make it easier it first takes the y and than the x so one can count the tiles in the more comfortable way x,y
        '''
        return self.tiles[x * TILE_SIZE : (x + 1) * TILE_SIZE, y * TILE_SIZE : (y + 1) * TILE_SIZE]

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
        # pink umbrella
        elif char == 'u':
            return self.get_tile_parameters(9, 2)
        # candy 1
        elif char == 'b':
            return self.get_tile_parameters(3,0)
        # candy 2
        elif char == 'c':
            return self.get_tile_parameters(3,1)

        else:
            return self.get_tile_parameters(2,1)


    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[
                    y * TILE_SIZE : (y + 1) * TILE_SIZE,
                    x * TILE_SIZE : (x + 1) * TILE_SIZE,
                ] = bm

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[
            OFS : OFS + self.image.shape[0], OFS : OFS + self.image.shape[1]
        ] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)

class Customer:

    def __init__(self, terrain_map, image, x, y):
        self.terrain_map = terrain_map
        self.image = image
        self.x = x
        self.y = y

    def __repr__(self):
        return(f'<Customer at {self.x}, {self.y}>')

    def draw(self, frame):
        x_pos = OFS + self.x * TILE_SIZE
        y_pos = OFS + self.y * TILE_SIZE
        frame[y_pos : y_pos + TILE_SIZE, x_pos : x_pos + TILE_SIZE] = self.image

    def move(self, direction):
        new_x = self.x
        new_y = self.y
        if direction == 'up':
            new_y -= 1
        elif direction == 'down':
            new_y += 1
        elif direction == 'left':
            new_x -= 1
        elif direction == 'right':
            new_x += 1

        if self.terrain_map.contents[new_y][new_x] == '.':
            self.x = new_x
            self.y = new_y

if __name__ == "__main__":

    background = np.zeros((700, 1000, 3), np.uint8)
    tiles = cv2.imread("./graphics/tiles.png")

    market = SupermarketMap(MARKET, tiles)

    # instantiate a customer
    customer = Customer(market, tiles[7 * TILE_SIZE : 8 * TILE_SIZE, : TILE_SIZE], 2, 2)

    while True:
        frame = background.copy()
        market.draw(frame)
        customer.draw(frame)

        cv2.imshow("frame", frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == 'w':
            customer.move('up')
        elif key == 'a':
            customer.move('left')
        elif key == 'd':
            customer.move('right')
        elif key == 's':
            customer.move('down')

        if key == "q":
            break

    cv2.destroyAllWindows()

    market.write_image("./graphics/supermarket.png")
