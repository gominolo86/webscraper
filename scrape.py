import requests
from bs4 import BeautifulSoup

url = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'

r = requests.get(url)
if r.status_code == 200:
    soup=BeautifulSoup(r.text,'html.parser')
    print("The title is ",soup.title.string)
    print("The author is ", soup.find(rel="author").get_text())
    #print(soup.get_text())
else:
    print('Error ', r.status_code)
