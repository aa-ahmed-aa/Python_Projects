from PIL import Image

img1 = Image.open("55.jpg")

res = img1.resize((100,100))
fliped=img1.transpose(Image.FLIP_LEFT_RIGHT)
spined=img1.transpose(Image.ROTATE_90)
res.show()
fliped.show()
spined.show()