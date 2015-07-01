import requests
from bs4 import BeautifulSoup
import operator

def connect(url):
    word_list=[]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'title' : 'General-purpose programming language'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean(word_list)

# cleans the string from the symbole
def clean(word_list):
    cleaned_list=[]
    for word in word_list:
        symbloe = "~!@#$%^&*()_+?-<>\"|.*/,?"
        for  i in range(0,len(symbloe)):
            word=word.replace(symbloe[i],"")
        if len(word) > 0:
            print(word)
            cleaned_list.append(word)
    create_dict(cleaned_list)

# create aadictionaru of words
def create_dict(cleaned_list):
    word_count = {}
    for word in cleaned_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word]=1
    for key , value in sorted(word_count.items(),key=operator.itemgetter(1)):
        print(key , value)

connect('https://en.wikipedia.org/wiki/Python_%28programming_language%29')
