import re

text = "I like orange! I love orange!"
text = "orange! I love orange!"
result = re.match("orange", text)

# print(result.group())
# print(result.start())
# print(result.end())
# print(result.span())




text = "I like orange! I love orange!"
result = re.search("orange", text)
# print(result.group())
# print(result.start())
# print(result.end())
# print(result.span())



text = "I like orange! I love orange!"
# result = re.findall("orange", text)
# print(result)


text = "I like orange! I love orange!"
result = re.finditer("orange", text)
# for data in result:
#     print(data.group())
#     print(data.start())
#     print(data.end())
#     print(data.span())


text = """
[앵커]

바로 좀 팩트체크를 해 보겠습니다. 제모를 하면 마약검사에서 빠져나갈 수 있다. 연예인 마약사건과 맞물려서 이런 글들이 온라인에서 확산됐습니다. 수사기법을 비웃는 듯한 내용입니다. 팩트체크팀이 국립과학수사연구원의 도움을 받아서 확인을 했습니다. 결론은 마약 성분은 체모 외에도 온몸을 흔적을 남긴다는 겁니다.
오대영 기자 나와 있습니다. 구체적으로 어떤 글들이 퍼져 있습니까?

[기자]

전신 제모를 하면 문제가 없다. 염색, 탈색을 하면 된다. 눈썹은 검사해도 소용없다 등의 내용입니다.
포털사이트에서 마약 검사라고 검색을 하면 모발 검사 안 걸리는 법이라는 연관 검색어까지 뜹니다.
"""

print(re.sub("\[.*\]","",text))