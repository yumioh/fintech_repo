import requests, json
from bs4 import BeautifulSoup

#요청url을 get에 넣음
#해당하는 응답값을 받을 수 있음
data = requests.get("https://jsonplaceholder.typicode.com/posts")
#print(data.text)
result = json.loads(data.text)

#data.json파일 생성
# with open("data.json", "w") as json_file:
#     # json.dump(result, json_file)

#파일을 읽기 
with open("data.json", "r") as json_file:
    test = json.load(json_file)
print(test)

# for d in result:
#     print(d['title'])
#     print(d['id'])

#json 형태로 응답이 오면 사용 가능
result = data.json()
#print(result)



