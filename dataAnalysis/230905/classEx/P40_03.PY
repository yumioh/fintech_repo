import requests
from bs4 import BeautifulSoup

response = requests.get('https://crawlingstudy-dd3c9.web.app/01')
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    url = 'https://crawlingstudy-dd3c9.web.app/01/' + link.attrs['href']
    response = requests.get(url)
    sub_page = BeautifulSoup(response.text, 'html.parser')
    print(sub_page.find('p').text.strip())
    # test = {'href': '01.html'}
    # test['href']