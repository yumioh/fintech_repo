import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
headers = {
    'authority:finance.naver.com'
    'method:GET'
    'path:/sise/sise_quant.nhn'
    'scheme:https'
    'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    'Accept-Encoding: gzip, deflate, br'
    'Accept-Language:ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    'Cookie:NNB=NY2O4PZCRXYWI; nx_ssl=2; page_uid=inj92lp0YihsscJPcMdssssstPs-264591; nid_inf=-1549333588; NID_JKL=BFpyzjvf668Nfvt/+SJuc+w+8C7bu5aM2jnJOtgdipQ=; naver_stock_codeList=252670%7C; JSESSIONID=9D125AAECB1F632E37D8A0C4C87F5066'
    'Sec-Ch-Ua:"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"'
    'Sec-Ch-Ua-Mobile:?0'
    'Sec-Ch-Ua-Platform:"Windows"'
    'Sec-Fetch-Dest:document'
    'Sec-Fetch-Mode:navigate'
    'Sec-Fetch-Site:none'
    'Sec-Fetch-User:?1'
    'Upgrade-Insecure-Requests:1'
    'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

bs = BeautifulSoup(response.text, "html.parser")
tbody = bs.select("table.type_2 tr")

for stock in tbody:
    for num in stock.select(".no"):
        number = num.text
    for val in stock.select("td a.tltle"):
        value = val.text
        for n in stock.select_one("td.number"):
            price = n
        print(number,value,price.replace(",",""))
