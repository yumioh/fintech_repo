import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")


popList = []
majorList = []

list_popCom = bs.select("ul.lst_pop > li a")
list_popPrice = bs.select("ul.lst_pop > li span")
list_majorCom = bs.select("ul.lst_major > li a")
list_majorPrice = bs.select("ul.lst_major > li span")

for val in list_popCom:
    company = val.text
    for val in list_popPrice:
        price = val.text
    popList.append([company,price])
print(popList)

for val in list_majorCom:
    company = val.text
    for val in list_majorPrice:
        price = val.text
    majorList.append([company,price])
print(majorList)

