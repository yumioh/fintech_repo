import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/01/')
soup = BeautifulSoup(res.text, 'html.parser')

titles = []
for link in soup.find_all('a'):
    url = 'https://crawlingstudy-dd3c9.web.app/01/' + link.attrs['href']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles.append(soup.find('title').text)

print(titles)