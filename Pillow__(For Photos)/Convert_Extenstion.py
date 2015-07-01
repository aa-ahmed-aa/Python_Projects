from PIL import Image
from PIL import ImageFilter

img = Image.open("55.jpg")

#convert the image to any
conv= img.convert("L")

#blur the image
blur= img.filter(ImageFilter.BLUR)

#flter the images
detail=img.filter(ImageFilter.DETAIL)

#edges filter
edges=img.filter(ImageFilter.FIND_EDGES)

conv.show()
blur.show()
detail.show()
edges.show()
