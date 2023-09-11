import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")

link = []

links = bs.select("body > a")

for x in links:
    name = x.text
    site = x.attrs['href']
    link.append({"name":name,"url":site})
print(link)