import requests
from bs4 import BeautifulSoup

def trader(max_pages):
    page= 1
    while page <= max_pages:
        url = 'https://egypt.dubizzle.com/ar/cairo/items-for-sale/search/?page='+str(page)
        source_code=requests.get(url)
        plain_text = source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'href':'title'}):
            href="https://egypt.dubizzle.com/" + link.get('href')
            title=link.string
            print(href)
            print(title)
        page += 1

trader(1)