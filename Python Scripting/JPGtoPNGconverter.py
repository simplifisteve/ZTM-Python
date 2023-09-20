import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(image_folder):
    print(f"Image folder {image_folder} does not exist")
    sys.exit()

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex/ folder and convert images to PNG format
for filename in os.listdir(image_folder):
    # check if it is a jpg image
    if filename.endswith(".jpg"):

        # get the image path
        img_path = f"{image_folder}/{filename}"

        # get the image name without extension
        img_name = os.path.splitext(filename)[0]

        # convert image to png
        img = Image.open(img_path)
        img.save(f"{output_folder}/{img_name}.png", "png")
