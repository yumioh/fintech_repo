import re

text = '''010-2334-3234
02-302-3033
010-1321-4043
02-01-32
33-3303-3033
016-444-3042'''

reg = '01[067]-[0-9]{3,4}-[0-9]{4}'
# for phone_number in re.finditer(reg, text):
#     print(phone_number.group())
#     print(phone_number.start())
#     print(phone_number.end())
#     print(phone_number.span())

print(re.sub(reg, '', text))

