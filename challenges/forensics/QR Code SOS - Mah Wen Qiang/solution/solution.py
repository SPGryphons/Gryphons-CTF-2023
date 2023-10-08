from PIL import Image
from itertools import combinations
import string
import random

img = Image.open('./Randomize.png')
size = w, h = img.size

white = (255, 255, 255)
black = (0, 0, 0)

newimg = Image.new(img.mode, img.size)
new = newimg.load()

data = img.load()

available_colors = [(254, 243, 0), (77, 109, 243), (153, 0, 49),
                    (110, 49, 152), (236, 28, 36), (34, 177, 76)]

for i in range(len(available_colors)):

    potential = combinations(available_colors, i+1)

    for good in potential:
        for x in range(w):
            for y in range(h):
                color = data[x, y]

                if color == white or color == black:
                    new[x, y] = color
                elif color in good:
                    new[x, y] = white
                else:
                    new[x, y] = black

        newimg.save(''.join([random.choice(string.ascii_lowercase)
                    for _ in range(10)]) + '.png')
