import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/01/')
soup = BeautifulSoup(res.text, 'html.parser')

#soup.find('table').find('tbody').find_all('tr')
#[<tr><td>이몽룡</td><td>34</td></tr>, <tr><td>홍길동</td><td>23</td></tr>]

students = []

for data in soup.find('table').find('tbody').find_all('tr'):

    #data.find_all('td')
    #[<td>이몽룡</td>, <td>34</td>]
    name = data.find_all('td')[0].text
    age = int(data.find_all('td')[1].text)
    students.append([name, age])

print(students)
