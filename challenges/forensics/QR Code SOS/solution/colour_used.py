from PIL import Image

img = Image.open('./Randomize.png')
size = w, h = img.size

white = (255, 255, 255)
black = (0, 0, 0)

newimg = Image.new(img.mode, img.size)
new = newimg.load()

data = img.load()

available_colors = []

for x in range(w):
    for y in range(h):
        color = data[x, y]
        if color not in available_colors:
            available_colors.append(color)

print(available_colors)
