from PIL import Image

first = Image.open("55.jpg")
second = Image.open("4.jpg")
area = (512,359,816,663)
second.paste(first,area)

second.show()