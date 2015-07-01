import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    FullName=str(name)+'.jpg'
    urllib.request.urlretrieve(url,FullName)

download_image("https://i.ytimg.com/vi/tVHWOurB6nc/default.jpg")