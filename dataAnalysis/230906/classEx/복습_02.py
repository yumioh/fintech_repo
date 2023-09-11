import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/01/')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find('p',id='hello').text.strip())