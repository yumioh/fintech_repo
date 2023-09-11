import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")


aptList = []
sale_items = bs.select(".sale_item")
sale_details = bs.select(".sale_detail > dl")


for names in sale_items:
    name = names.select_one("a").text #아파트 이름
    for details in sale_details:
        price = details.select_one(".point").text
        infos =  details.select(".txt")
        for idx,info in enumerate(infos):
            if info == "아파트":
                print("**")


        
aptList.append({"이름":name, "분양가":price})
#print(aptList)

    