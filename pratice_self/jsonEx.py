import requests, json
from bs4 import BeautifulSoup

url = "https://jsonplaceholder.typicode.com/photos"
response = requests.get(url)

print(response.text)
all_list = []

for value in response.json():
    comment_list = {
        "id": value['id'], 
        "title": value['title'],
        "comment":[]
    }

    comment_url = "https://jsonplaceholder.typicode.com/comments?postId=1"#+ str(id)
    comment_res = requests.get(comment_url)
    for comment in comment_res.json():
        comment_list['comment'].append(comment['body'])
    all_list.append(comment_list) 
#print(all_list)