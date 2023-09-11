import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01'

data = {
    'name':'jinbeom'
    }

headers  = {
    'Content-Type':'application/josn;charset=utf-8'
    }

#get 데이터 들고 오기 url값 
response = requests.get(URL,headers=headers,data=data)

soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("title")
print(result)
print(result.text)

# print(response.status_code)
print(response.text) #데이터값 출력
# print("오류확인")

