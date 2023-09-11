import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

#01
result = soup.find("h2").text
print(result)

#02
result2 = soup.find('p',id="hello").text.strip()
print(result2)

#03
students = []

#리스트값 
datas = soup.find('table').find('tbody').find_all('tr')
for data in datas:
    # [이몽룡, 32]
    name = data.find_all('td')[0].text
    age = int(data.find_all('td')[1].text)
    students.append([name,age])
print(students)

#이몽룡[0][1]
# 34[0][1]
# 홍길동[1][0]
# 23[1][1]

#04
links = soup.find_all("a")

names = []
for name in links:
   hrefName = name.attrs['href']
   #hrefName = name.get('href')
   newURL = URL + "/"+ hrefName
   response = requests.get(newURL)
   newSoup = BeautifulSoup(response.text, "html.parser")
   title = newSoup.find("title").text
   names.append(title)
print(names)


