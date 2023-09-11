import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01'

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
#result = soup.find("title")

soup.find("p")

#result = soup.find_all("th","tablehead") #tablehead라는 클래스 갖고 옴
#result = soup.find("th",class_= "tablehead")

#딕셔너리 형태로 넣음
#result = soup.find("th", attrs={"class":"tablehead"})
#result = soup.find("h1", attrs={"title":"welcome"})
result = soup.find_all(id="hello")


#print(result) #tag가 포함된 결과값
#print(result.text) # tag가 제외된 결과값
for element in result:
    print(element.text.strip())

# result1 = soup.find("table")
# result2 = result1.find("tbody")
# print(result2)


result3 = soup.find("table").find("tbody")
print(result3)

result4 = soup.find("a")
print(result4.text)
print(result4.attrs['href'])