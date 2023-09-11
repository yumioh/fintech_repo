import requests, json
from bs4 import BeautifulSoup

#메인 get의 response
response = requests.get("https://jsonplaceholder.typicode.com/photos")
soup = BeautifulSoup(response.text, "html.parser")

site_dict = []
#id/ title 값 추출
#print(soup.text)
site_json = json.loads(soup.text)
for val in site_json:
    id = val['id']
    title = val['title']
    site_dict.append({"id":id,"title":title,"commnent":[]})
    content_res = requests.get("https://jsonplaceholder.typicode.com/comments?postId=" + str(val['id']))
    for con in content_res.json():
        body = con["body"].replace("\n","")
    break
#print(site_dict)
