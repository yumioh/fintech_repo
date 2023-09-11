import re

text= """
<p>
<span>네이버가 뉴스 서비스에 인공지능(AI)을 도입해 페이지 뷰(PV)를 늘리고 이용자를 끌어 모으고 있다.</span>
<span>네이버는 5일 오전 서울 강남구 그랜드 인터컨티넨털 호텔에서 AI 콜로키움 2019를 열고 이 같은 AI 성과와 전략을 소개했다.</span>
<span>이날 기조연설에서 김광현 네이버 서치앤클로바 리더는 "AI 뉴스 추천 시스템인 에어스(AiRS)를 도입하면서 뉴스 소비량이 확대되고 있다" 고 말했다.</span>
</p>

"""
#특정 태그 추출하여 텍스트 뽑기
#reg1 = "<span(.*?)>(.*?)<\/span>"
#span태그에 포함된거 뽑기
reg1 = "<span>.*<\/span>"
reg2 = "<[^>]*>" # = <\/*span>

results = re.finditer(reg1,text)

tag_list = []
for result in results:
    group_txt = result.group()
    result2 = re.sub(reg2,"",group_txt)
    tag_list.append(result2)
print(tag_list)
#     print(result.group())
    #tag_list.append(result.group())
#print(tag_list)