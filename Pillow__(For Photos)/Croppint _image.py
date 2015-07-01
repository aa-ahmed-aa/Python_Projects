from PIL import Image

img = Image.open('4.jpg')

area_crpoing = (100,100,300,300)

new_image = img.crop(area_crpoing)

img.show()
new_image.show()