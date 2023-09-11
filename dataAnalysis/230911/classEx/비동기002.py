import requests
import json

res = requests.get('https://jsonplaceholder.typicode.com/photos')

all_data = []

for data in res.json():
    comment_url = 'https://jsonplaceholder.typicode.com/comments?postId=' + str(data['id'])
    comment_url = f'https://jsonplaceholder.typicode.com/comments?postId={data["id"]}'
    comment_res = requests.get(comment_url)

    comment_data = {
        'id': data['id'],
        'title': data['title'],
        'comment': []
    }

    for comment in comment_res.json():
        comment_data['comment'].append(comment['body'].replace('\n',''))

    all_data.append(comment_data)

with open('data2.json', 'w') as f:
    json.dump(all_data, f)
    