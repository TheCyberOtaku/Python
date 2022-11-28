from PIL import Image
from PIL import ImageChops
import os

#opens all pngs in the folder and trims transparent pixels
def trim_all():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".png"):
            im = Image.open(file)
            im.load()
            bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
            diff = ImageChops.difference(im, bg)
            diff = ImageChops.add(diff, diff, 2.0, -100)
            bbox = diff.getbbox()
            im = im.crop(bbox)
            im.save(file)

trim_all()