from PIL import Image

img = Image.open("54.jpg")
r,g,b = img.split()

r.show()
g.show()
b.show()

