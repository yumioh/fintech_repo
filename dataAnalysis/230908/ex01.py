import re

#reg = ".+[@].+(.com|.kr)"
#이메일
reg = '[a-zA-Z]+@[a-zA-z]+(\.[a-z]{2,4}){1,2}'

text = """
jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr
"""

results = re.finditer(reg, text)
#print(result)

for result in results:
    print(result.group())