from PIL import Image

img = Image.open("2.jpg")
print(img.size)
print(img.format)

img.show()