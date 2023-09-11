import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.jungle.co.kr/')
bs = BeautifulSoup(res.text, 'html.parser')

for data in bs.select('ul.thumb_list li'):
    try:
        print(data.select_one('span.title').text)
        print(data.select_one('a.thumb_cate').text)
    except:
        pass

#-------------------------------------------------------#

params = {
    'magazineOffset':0,
    'contestOffset':0,
    'exhibitOffset':0,
    'galleryOffset':0
}

#print(params)
for i in range(5):
    res = requests.get('https://www.jungle.co.kr/recent.json', params=params)

    for data in res.json()['moreList']:
        print(data['title'])
        print(data['targetCode'])

    params['magazineOffset'] = res.json()['magazineOffset']
    params['contestOffset'] = res.json()['contestOffset']
    params['exhibitOffset'] = res.json()['exhibitOffset']
    params['galleryOffset'] = res.json()['galleryOffset']
#print(params)