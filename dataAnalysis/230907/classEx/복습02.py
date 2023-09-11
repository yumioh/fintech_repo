import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/02')
soup = BeautifulSoup(res.text,'html.parser')

#[<li class="blue">두번째리스트</li>, <li class="blue">세번째리스트</li>]
for value in soup.select('div#content > ul > li.blue'):
    print(value.text)
