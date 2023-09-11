import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/02/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")

body = bs.select_one("body #winter")
friend = body.select_one("div")
print(friend.select_one('p.blue').text)

bs.select_one("div#winter > div > p.blue")
bs.find("div", id="winter").find("div").find("p", class_="blue").text