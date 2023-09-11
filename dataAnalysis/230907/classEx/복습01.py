import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text,'html.parser')

print(soup.select('#title')[0].text.strip())
print(soup.select_one('#title').text.strip())
print(soup.select('div.bold.blue')[0].text.strip())
print(soup.find('div',id='title').text.strip())
