import requests
import re
from bs4 import BeautifulSoup

for page in range(1, 11):

    params = {
        'd_cat_cd':'001',
        'brand':'',
        'list_kind':'small',
        'sort':'pop_category',
        'sub_sort':'',
        'page':page,
        'display_cnt':'90',
        'group_sale':'',
        'exclusive_yn':'',
        'sale_goods':'',
        'timesale_yn':'',
        'ex_soldout':'',
        'plusDeliveryYn':'',
        'kids':'',
        'color':'',
        'price1':'',
        'price2':'',
        'shoeSizeOption':'',
        'tags':'',
        'campaign_id':'',
        'includeKeywords':'',
        'measure':''
    }

    res = requests.get('https://www.musinsa.com/categories/item/001', params=params)
    #print(res.text)
    bs = BeautifulSoup(res.text, 'html.parser')

    for data in bs.select('#searchList li.li_box'):
        brand = data.select_one('.item_title a').text.strip()
        name = data.select('p.list_info')[0].text.strip()
        price = str(data.select_one('.price'))
        price = re.sub('<del>.*<\/del>','',price)
        price = re.sub('<[^>]*>','',price).strip()
        
        print('브랜드 : ', brand)
        print('제품명 : ', name)
        print('가격 : ', price)
        print()