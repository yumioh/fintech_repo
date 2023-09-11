import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/03/')
bs = BeautifulSoup(res.text, 'html.parser')


lis = bs.select('ul.lst_pop > li')

pops = []
for li in lis:
    # print(li.select('a')[0].text)
    # print(li.select('span')[0].text)
    name = li.select_one('a').text
    score = li.select_one('span').text
    pops.append([name, score])

print(pops)


lis = bs.select('ul.lst_major > li')

lst_major = []

for li in lis:
    name = li.select_one('a').text
    score = li.select_one('span').text
    lst_major.append([name, score])

print(lst_major)