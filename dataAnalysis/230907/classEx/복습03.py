import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text,'html.parser')

print(soup.select_one('div#winter > div > p.blue').text)
print(soup.find('div', id='winter').find('div').find('p',class_='blue').text)