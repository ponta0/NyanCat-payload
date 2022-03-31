import sys
import math
from PIL import Image

doscolors = [
	(0x00, 0x00, 0x00), # 0
	(0x00, 0x00, 0xa8), # 1
	(0x00, 0xa8, 0x00), # 2
	(0x00, 0xa8, 0xa8), # 3
	(0xa8, 0x00, 0x00), # 4
	(0xa8, 0x00, 0xa8), # 5
	(0xa8, 0xa8, 0x00), # 6
	(0xa8, 0xa8, 0xa8), # 7
	
	(0x54, 0x54, 0x54), # 8
	(0x54, 0x54, 0xff), # 9
	(0x54, 0xff, 0x54), # 10
	(0x54, 0xff, 0xff), # 11
	(0xff, 0x54, 0x54), # 12
	(0xff, 0x54, 0xff), # 13
	(0xff, 0xff, 0x54), # 14
	(0xff, 0xff, 0xff), # 15
]

def color_distance(c1, c2):
	return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2)

def nearest_color(c):
	nearest = 0
	for i in range(len(doscolors)):
		if color_distance(c, doscolors[i]) < color_distance(c, doscolors[nearest]):
			nearest = i
	return nearest

buf = bytearray()

for imgf in sys.argv[1:-1]:
	img = Image.open(imgf)
	img = img.convert("RGB")
	
	width, height = img.size
	
	for y in range(0, height, 2):
		for x in range(width):
			b = nearest_color(img.getpixel((x, y))) << 4 | nearest_color(img.getpixel((x, y + 1)))
			buf.append(b)

with open(sys.argv[-1], "wb") as f:
	f.write(buf)