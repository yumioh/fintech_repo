import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/03/')
bs = BeautifulSoup(res.text, 'html.parser')

pops = []
for data in bs.select('ul#popularItemList li'):
    name = data.select_one('a').text
    alt = data.select_one('img').attrs['alt']

    # if alt == '상승':
    #     alt = '상한'
    # elif alt == '하락':
    #     alt = '하한'

    alt = alt.replace('상승','상한').replace('하락','하한')
    pops.append([name, alt])
    #print(name, alt)

print(pops)

lst_major = []
for data in bs.select('ul.lst_major li'):
    name = data.select_one('a').text
    alt = data.select_one('img').attrs['alt']
    alt = alt.replace('상승','상한').replace('하락','하한')
    lst_major.append([name, alt])
    #print(name, alt)

print(lst_major)