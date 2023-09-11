import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")

#03

popList3 = []
majorList3 = []

list_popCom3 = bs.select(".lst_pop > li a")
list_popPrice3 = bs.select(".lst_pop > li span")
list_popUpDown3 = bs.select(".lst_pop > li img")
list_majorCom3 = bs.select(".lst_major > li a")
list_majorPrice3 = bs.select(".lst_major > li span")
list_majorUpDown3 = bs.select(".lst_major > li")
print(list_popUpDown3)

for val in list_popCom3:
    company3 = val.text
    for val in list_popUpDown3:
        up2 = val.select('img[alt="상승"]')
        print(up2)
       # for val in list_popPrice:
      #      price = val.text
    #popList3.append([company,price])
#print(popList3)

for val in list_majorCom3:
    company3 = val.text
    for val in list_majorPrice3:
        price3 = val.text
    majorList3.append([company3,price3])
print("-------------------------------")      
#print(majorList3)