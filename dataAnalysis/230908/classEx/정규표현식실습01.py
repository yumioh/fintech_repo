import re

text = '''jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr'''

for email in re.finditer('[a-zA-Z]+@[a-zA-Z]+(\.[a-z]{2,4}){1,2}', text):
    print(email.group())

