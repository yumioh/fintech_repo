import requests
from bs4 import BeautifulSoup

response = requests.get('https://crawlingstudy-dd3c9.web.app/01')
soup = BeautifulSoup(response.text, 'html.parser')

students = []
head = []

results = soup.find('table').find_all('th')
for result in results:
    head.append(result.text)

datas = soup.find('table').find('tbody').find_all('tr')
for data in datas:
    name = data.find_all('td')[0].text
    age = data.find_all('td')[1].text
    # students.append({
    #     head[0]:name,
    #     head[1]:age
    # })

    # students.append(dict(zip(head, [name,age])))

    students.append({
        '이름':name,
        '나이':age
    })

print(students)