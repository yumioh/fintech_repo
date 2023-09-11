import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")

#02
popList2 = []
majorList2 = []

list_popCom2 = bs.select(".lst_pop > li a")
list_popUpDown2 = bs.select(".lst_pop > li")
list_majorCom2 = bs.select(".lst_major > li a")
list_majorUpDown2 = bs.select(".lst_major > li")

for val in list_popCom2:
    company2 = val.text
    for val in list_popUpDown2:
        #up1 = val.select_one('img[alt="상승"]')
        up2 = val.select_one('img').attrs['alt']
        print(up2)
        if up2 == "상한" or up2 =="상승":
            status = "상한"
        else :
            status = "하한"
    popList2.append([company2,status])
print(popList2)

for val in list_majorCom2:
    company = val.text
    for val in list_majorUpDown2:
        up1 = val.select('img[alt="상승"]')
        up2 = val.select('img[alt="상한"]')
        if up1 or up2 != []:
            status = "상한"
        else :
            status = "하한"
    #majorList2.append([company,status])
#print(majorList2)
