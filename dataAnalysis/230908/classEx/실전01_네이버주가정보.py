import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/sise_quant.nhn')
bs = BeautifulSoup(res.text, 'html.parser')

# x = [1, 2, 3, 4, 5, 6]
# print(x[1:])

for tr in bs.select('table.type_2 > tr')[1:]:
    if len(tr.select('td')) != 1:
        # if len(tr.select('span.red02')) > 0:
        #     print(tr.select('td')[0].text, tr.select('td')[1].text, tr.select('td')[2].text, tr.select('td')[3].text.strip())
        
        # if len(tr.select('td')[3].select('img')) > 0 and tr.select('td')[3].select_one('img').attrs['src'].find('up'):
        #     print(tr.select('td')[0].text, tr.select('td')[1].text, tr.select('td')[2].text, tr.select('td')[3].text.strip())

        if len(tr.select('td')[3].select('img')) > 0 and tr.select('td')[3].select_one('img[src*="up"]') != None:
              print(tr.select('td')[0].text, tr.select('td')[1].text, tr.select('td')[2].text, tr.select('td')[3].text.strip())
