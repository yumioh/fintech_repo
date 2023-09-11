import requests
from bs4 import BeautifulSoup

URL ="https://crawlingstudy-dd3c9.web.app/02"

reponse = requests.get(URL)
bs = BeautifulSoup(reponse.text, "html.parser")

# select : 셀렉에 일치하는 모든 태그 불려옴 - > 리스트 형태로 출력
#bs.find(id="title")
result = bs.select("#title")
result2 = bs.select_one("#title")
#print(result)
print(result[0].text.strip())
# 셀렉터에 일치하는 하나의 태그만 
print(result2.text.strip())

#select(태그명)
#find_all(태그명)
print(bs.select("title")[0].text.strip())

#클래스명 들고 오기 .클래스명
# print(bs.select(".bold"))
# print(bs.find_all(class_='bold'))

#후손셀렉터
#p 아래에 자손 태그 내용 출력
# print(bs.select("div#winter p"))
# print(bs.find("div", id="winter").find_all("p"))

print(bs.select("div#winter > p"))

