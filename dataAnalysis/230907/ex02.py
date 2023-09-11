import requests,re
from bs4 import BeautifulSoup

#URL = 'https://www.musinsa.com/categories/item/001'
for i in range(0,11):
    URL ='https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page='+ str(i) +'&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
    response = requests.get(URL)
    bs = BeautifulSoup(response.text, "html.parser")
    #get 방식인 경우 data는 params로 보내야함 prams=data

#response = requests.get(URL)
#bs = BeautifulSoup(response.text, "html.parser")


for items in bs.select("#goods_list"):
    for item in items.select(".article_info"):
        brand = item.select_one("p.item_title > a").text.strip()
        product = item.select_one("p.list_info > a").text.strip()
        #for id, val in enumerate(item.select("p.price")):
        price = str(item.select_one("p.price"))
        price = re.sub("<del>.*<\/del>",'', price) #del 태그 지움
        price = re.sub("<[^>]*>",'', price).strip() # 나머지 태그 지움
       # for idx in enumerate(prices):
       #     if idx != []:
       #         price = prices[0]
       #     else :
       #         price = prices[1]
        print("""브랜드: {} 
               제품명: {} 
               가격 : {}"""
               .format(brand, product,price))