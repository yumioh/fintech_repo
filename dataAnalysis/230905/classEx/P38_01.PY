import requests
from bs4 import BeautifulSoup

response = requests.get('https://crawlingstudy-dd3c9.web.app/01')
soup = BeautifulSoup(response.text, 'html.parser')

cook = soup.find(id='cook')
print(cook.text.strip())