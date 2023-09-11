import requests
from bs4 import BeautifulSoup

res = requests.get('https://crawlingstudy-dd3c9.web.app/03')
soup = BeautifulSoup(res.text,'html.parser')

all_data = []

for data in soup.select('body > ul.sale_list > li'):
    name = data.select_one('div.sale_tit > a').text.strip()
    detail = data.select('dl.detail_info dd')
    #[
    # <dd class="txt"><strong class="point">45,600</strong> 만원</dd>,
    # <dd class="txt">아파트<span class="bar">|</span>장기전세주택</dd>,
    # <dd class="txt">분양 1세대<span class="bar">|</span>150㎡</dd>,
    # <dd class="txt">서울시 송파구 마천동</dd>
    # ]
    price = detail[0].text.replace(',','').replace(' 만원','').strip()
    type = detail[1].text.split('|')
    type1 = type[0]
    type2 = type[1]
    option = detail[2].text.split('|')
    option1 = option[0]
    option2 = option[1]
    #{'이름': 'H하우스장위',  '분양가': '16000',  '유형': '아파트',  '분양유형': '일반민간임대',  '세대수': '분양 134세대',  '평형': '45㎡~65㎡'},
    all_data.append({
        '이름':name,
        '분양가':price,
        '유형':type1,
        '분양유형':type2,
        '세대수':option1,
        '평형':option2
    })
    #print(name, price, type1, type2, option1, option2)

print(all_data)
