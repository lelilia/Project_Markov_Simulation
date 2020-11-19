import numpy as np
import cv2

# local import
from tiles import SupermarketMap
from customer import Customer
from utils.constances import MARKET, TILES

if __name__ == "__main__":

    background = np.zeros((700, 1000, 3), np.uint8)
    # tiles = cv2.imread("./graphics/tiles.png")

    market = SupermarketMap(MARKET, TILES)

    # instantiate a customer
    # customer = Customer(market, tiles[7 * TILE_SIZE : 8 * TILE_SIZE, : TILE_SIZE], 2, 2)

    while True:
        frame = background.copy()
        market.draw(frame)
        # customer.draw(frame)

        cv2.imshow("frame", frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        # if key == 'w':
        #     customer.move('up')
        # elif key == 'a':
        #     customer.move('left')
        # elif key == 'd':
        #     customer.move('right')
        # elif key == 's':
        #     customer.move('down')

        if key == "q":
            break

    cv2.destroyAllWindows()

    market.write_image("./graphics/supermarket.png")
