import requests
import csv
from bs4 import BeautifulSoup

file = open("stock.csv", mode="w", encoding="utf-8", newline="")
writer = csv.writer(file)

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

for page in range(2, 5):

    params = {
        'code':'005930',
        'page':page
    }

    response = requests.get(f'https://finance.naver.com/item/sise_day.naver', params=params, headers=headers)
    bs = BeautifulSoup(response.text, 'html.parser')

    for tr in bs.select('table.type2 tr'):
        if len(tr.select('td')) >= 7:
            writer.writerow([tr.select('td')[0].text.replace('.','-'),
                             tr.select('td')[1].text.replace(',','')])

file.close()