import requests
import pandas as pd
from bs4 import BeautifulSoup

test_url = 'https://blog.naver.com/aaa4815926/223217855620'

#블로그 페이지 정보 가져오기 
def get_blog(url) :
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 
       'Referer' : 'https://search.naver.com/search.naver?where=news&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&sort=2&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0'}
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text,'html.parser')

  #blog iframe 값 불려 오기
  blog = soup.select_one('iframe').attrs['src']
  blog_url = 'https://blog.naver.com'+ blog

  blog_res = requests.get(blog_url)
  blog_soup = BeautifulSoup(blog_res.text,'html.parser')

  #블로그 카테고리, 제목, 작성자, 시간, 내용 추출
  category = blog_soup.select_one('div.blog2_series a').text.strip()
  #title = blog_soup.select_one('span.se-fs-.se-ff-').text.strip()
  writer = blog_soup.select_one('span.nick a').text.strip()
  time = blog_soup.select_one('span.se_publishDate.pcol2').text.strip()
  content = blog_soup.select_one('div.se-main-container').text.strip().replace('\u200b','').replace('\n','')
  return(category, writer, time, content)

def get_blog_list(keyword, startDate, endDate) :
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 
            'Referer' : 'https://search.naver.com/search.naver?where=news&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&sort=2&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0'}

    blog_list_url = 'https://search.naver.com/search.naver?where=view&query="{0}"&sm=tab_opt&nso=so%3Add%2Cp%3Afrom{1}to{2}a&mode=normal&main_q=&st_coll=&topic_r_cat='.format(keyword, startDate, endDate)
    res = requests.get(blog_list_url, headers=headers)
    blog_bs = BeautifulSoup(res.text,'html.parser')
    #print(blog_list_url)

    li = []
    for blogs in blog_bs.select('ul.lst_total._list_base li'):
        url = blogs.select_one('a.api_txt_lines').attrs['href']
        if url.split('/')[2].startswith('blog') :
           li.append(get_blog(url))

    return pd.DataFrame(li, columns=['category', 'writer', 'time', 'content'])

    
test = get_blog('https://blog.naver.com/soryu6964/223218016383')
print(get_blog_list('테슬라','20230920','20230921'))