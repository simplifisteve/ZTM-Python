import sys
import os
from PIL import Image

# grab the first and second argument
sys.argv[1] = '/Users/simplifisteve/ZTM Python/Python Scripting/image_processing/pokedex'
sys.argv[2] = '/Users/simplifisteve/ZTM Python/Python Scripting/image_processing/new'

# check if new/ exists, if not create it
if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

# loop through pokedex/ folder and convert images to PNG format
for filename in os.listdir(sys.argv[1]):
    # check for jpg extension
    if filename.endswith(".jpg"):
        # get path to image
        img_path = f"{sys.argv[1]}/{filename}"
        # get name of image without extension
        img_name = os.path.splitext(filename)[0]
        # convert image to png
        img = Image.open(img_path)
        img.save(f"{sys.argv[2]}/{img_name}.png", "png")
