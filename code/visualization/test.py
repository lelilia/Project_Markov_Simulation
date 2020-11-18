from PIL import Image
import numpy as np

im = Image.open('graphics/supermarket.png')
market = np.array(im)
print(market.shape, market.dtype)

im2 = Image.open('graphics/tiles.png')
tiles = np.array(im2)

x = 4 * 32
y = 1 * 32

apple = tiles[y:y+32, x:x+32]

tx = 13*32
ty = 2 * 32

market[ty:ty+32, tx:tx+32] = apple

im = Image.fromarray(market)
im.save('supermarket_filled.png')