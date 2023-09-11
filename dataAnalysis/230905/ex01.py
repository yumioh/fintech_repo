import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

##01 
result1 = soup.find(id="cook")
print(result1.text.strip())

##02
table = soup.find("table")
tabHaed = table.find_all("th")
tabBody = table.find("tbody").find_all("tr")

head = []
students =[]

for result in tabHaed:
    head.append(result.text)

for data in tabBody:
    name = data.find_all("td")[0].text
    age = data.find_all("td")[1].text
 #   students.append({
 #       head[0]:name,
 #       head[1]:age
 #   })
    students.append(dict(zip(head, [name,age])))
    # students.append({
    #     '이름':name,
    #     '나이':age
    # })

#print(students)



## 03
aLinkPage = soup.find_all("a")
#print(aLinkPage)
for link in aLinkPage:
    newUrl = URL+"/" + link.get("href")
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "html.parser")
    result2 = soup.find("body").find("p").text.strip()
   # print(result2)
    #print(link.text.strip(), link.get("href"))