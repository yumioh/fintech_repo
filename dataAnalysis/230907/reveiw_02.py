import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")


body = bs.select_one("body")
result = body.select("li.blue")
#class="bold blue" -> .bold.blue 표현
for i in result:
    print(i.text)