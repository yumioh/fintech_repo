import requests
from bs4 import BeautifulSoup

headers = {
    #':authority':'finance.naver.com',
    #':method':'GET',
    #':path':'/sise/sise_quant.nhn',
    #':scheme':'https',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control':'max-age=0',
    'Cookie':'NNB=G73XACG5Z73WI; naver_stock_codeList=252670%7C; JSESSIONID=90C383359E2C01837AA9EBBCE9378F8E',
    'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"macOS"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

res = requests.get('https://finance.naver.com/sise/sise_quant.nhn',headers=headers)
bs = BeautifulSoup(res.text, 'html.parser')
#print(res.text)
#print(bs.select('table.type_2 > tr')[1:])
for data in bs.select('table.type_2 > tr'):
    if data.select_one('th') == None and len(data.select('td')) == 12:
        print(data.select('td')[1].text)
    #print(data)