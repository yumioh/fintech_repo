import requests, json
from bs4 import BeautifulSoup

url = "https://www.jungle.co.kr/"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

#제품 목록 화면
for value in bs.select("div.container_main li"):
    print(value)
    # title = value.select_one("span.title").text
    # category = value.select_one("a.thumb_cate").text
    # print(title)
    # print(category)
    # for title in value.select("span.title"):
    #     title = title.text
    # for categories in value.select("a.thumb_cate"):
    #     category = categories.text
    #     print(category)


   #title, category 가져오기
#    category = value.select_one("a.thumb_cate")
  # print(title.text)
  # print(category.text)
  #print(value)

#    for titles in value.select("a.thumb_title span.title"):
    # print(titles.text)
#    for idx, categories in enumerate(value.select("li > a.thumb_cate")):
#     print(idx, categories.text)

      
