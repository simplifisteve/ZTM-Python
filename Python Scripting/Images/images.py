from PIL import Image

img = Image.open(
    '/Users/simplifisteve/ZTM Python/Python Scripting/image_processing/astro.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L') # convert to black & white
# resize = filtered_img.resize((300,300))
# filtered_img = img.filter(ImageFilter.SMOOTH)
# rotated = filtered_img.rotate(180)

# filtered_img.save("blur.png", 'png') # convert to PNG
# filtered_img.save("smooth.png", 'png')
# print(dir(img)) # to see all the command options
# rotated.save("rotated_smooth.png", 'png')

img.thumbnail((500, 500))  # use thumbnail to resize and keep aspect ratio
img.save("thumbnail_astro.jpg")
