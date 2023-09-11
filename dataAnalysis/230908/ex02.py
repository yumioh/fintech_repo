import re

#reg = "(<([^>]+)>)"

reg = "<[^>]*>"

text = """
안녕하세요 저는 <em>홍길동</em> 입니다. 나이는 24살 세계 최고의 <a href="aa.aa.com">데이터 분석가</a>가 되고싶습니다.
"""
#텍스트 안 태그 제거
result= re.sub(reg,"",text)
print(result)