
from PIL import ImageGrab

box = (1, 2, 3, 2)

image = ImageGrab.grab(box)


image.save('xx.png')