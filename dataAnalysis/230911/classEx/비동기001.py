import requests
import json

#res = requests.get('https://crawlingstudy-dd3c9.web.app/04/')

data = requests.get('https://jsonplaceholder.typicode.com/posts')
# result = json.loads(data.text)
# for d in result:
#     print(d['title'])
#     print(d['body'])
#     print()

result = data.json()

# with open('data.json', 'w') as json_file:
#     json.dump(result, json_file)

with open('data.json', 'r') as json_file:
    test = json.load(json_file)

print(test)