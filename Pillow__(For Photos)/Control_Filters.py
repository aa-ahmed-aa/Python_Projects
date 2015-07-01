from PIL import Image

#merging to images but they should be at the same size
img1 = Image.open("55.jpg")
img2 = Image.open("77.jpg")
r1 , g1 , b1 = img1.split()
r2 , g2 , b2 = img2.split()

new_image=Image.merge("RGB",(b2,g2,b1))
new_image.show()

# combine and merge filters
'''
img = Image.open("54.jpg")
r,g,b = img.split()
new_image = Image.merge("RGB",(r,g,b))
new_image.show()
'''