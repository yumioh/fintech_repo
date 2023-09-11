import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")

hello = bs.select_one("body").select_one("#title").text.strip()
print(hello)