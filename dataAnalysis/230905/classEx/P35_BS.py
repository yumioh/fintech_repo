#BeautifulSoup 실습

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01'
response = requests.get(URL)

bs = BeautifulSoup(response.text, 'html.parser')
#result = bs.find('title')
#result = bs.find_all('th', 'tablehead')
#result = bs.find_all('th', class_='tablehead')
#result = bs.find_all('th', attrs={'class':'tablehead'})
#result = bs.find_all('h1', attrs={'title':'welcome'})
result = bs.find_all(id='hello')

#print(result)

for element in result:
    print(element)
    print(element.text.strip())


# result1 = bs.find('table')
# result2 = result1.find('tbody')
#print(result2)

# result = bs.find('table').find('tbody')
# print(result)

result = bs.find('a')
print(result.text)
print(result.attrs['href'])