import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text,'html.parser')

soup.find_all('a')

all = []

for value in soup.select('a'):
    name = value.text
    url = value.attrs['href']
    all.append([name, url])

print(all)