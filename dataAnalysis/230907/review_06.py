import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
bs = BeautifulSoup(response.text, "html.parser")

apt_list = []
apt_items= bs.select("body ul.sale_list")
for item in apt_items:
    for sale in item.select(".sale_item"):
        name = sale.select_one('a[target="_blank"]').text
        point = sale.select_one(".point").text
        for details in sale.select(".detail_info"):           
           categories = details.select("dd")[1].text
           cat = categories.split("|")        
           sizes = details.select("dd")[2].text
           size = sizes.split("|")
        apt_list.append({"아파트":name, "분양가":point.replace(",",""),"유형":cat[0],"분양유형":cat[1],"세대수":size[0],"평형":size[1]})
print(apt_list)
