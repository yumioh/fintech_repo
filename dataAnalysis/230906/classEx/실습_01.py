import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
bs = BeautifulSoup(res.text, 'html.parser')

#bs.find_all(id='title')

#b = ['abc']
#b[0].replace('abc','ccd')

# print(bs.select('#title')[0].text.strip())
# print(bs.select_one('#title').text.strip())

# print(bs.find_all('title')[0].text) #여러개
# print(bs.find('title').text) #한개
# print(bs.select('title')[0].text) #여러개
# print(bs.select_one('title').text) #한개

# print(bs.find_all(class_='bold'))
# print(bs.select('.bold'))
# print(bs.find('div', id='winter').find_all('p'))
# print(bs.select('div#winter p'))

print(bs.select('div#winter > p'))