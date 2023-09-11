import requests,re
from bs4 import BeautifulSoup

page = 1
while True:
    URL = 'https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003&date=20230910&page='+str(page)

    headers = {
    # 'authorit':'gfp.veta.naver.com',
    # 'method':'GET',
    # 'path':'/call?u=p_news_sidebox&xdid=glad_ad_sidebox&p=calp%3Ashome%2Cda_dom_id%3Aglad_ad_sidebox&iv=6f262964-b2e4-404e-b0b5-acba69bfc94a&ivt=0&c=https%3A%2F%2Fnews.naver.com%2Fmain%2Flist.naver%3Fmode%3DLPOD%26mid%3Dsec%26oid%3D003&sv=2.19.2&sn=web&an=news.naver.com&sa=0&nt=0&rui=97755445631739620',
    # 'scheme':'https',
    # 'Accept':'application/json, text/plain, */*',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'AcceptLanguage':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie':'NNB=NY2O4PZCRXYWI; nx_ssl=2; page_uid=inj92lp0YihsscJPcMdssssstPs-264591; nid_inf=-1549333588; NID_JKL=BFpyzjvf668Nfvt/+SJuc+w+8C7bu5aM2jnJOtgdipQ=',
    # 'Origin':'https://news.naver.com',
    # 'Referer':'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003',
    # 'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    # 'Sec-Ch-Ua-Mobile':'?0',
    # 'Sec-Ch-Ua-Platform':'"Windows"',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-site',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)
    bs = BeautifulSoup(response.text, "html.parser")
    now_page= bs.select_one("div.pageing strong")

    if page != now_page:
        break


news = bs.select("ul.type06_headline > li > dl > dt")
news_list = []
for val in news:
    news_url = val.select_one("a").attrs["href"]
    #print(news_url)
    response2 = requests.get(news_url,headers=headers)
    newBS = BeautifulSoup(response2.text, "html.parser")
    news_title = newBS.select_one(".media_end_head_title")
    news_content = newBS.select_one(".go_trans._article_content")
        #news_list.append([news_title.text.strip(), news_content.text.strip().replace("\n","").replace("\'","")])
    if news_title is not None:
        for title in news_title:
            for content in news_content:
                news_content = content.text.strip()
                news_list.append([title.text.strip(), news_content.replace("\n","").replace("\'","")])
print(news_list)

page += 1




    