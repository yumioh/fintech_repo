import re

numbers = """
010-2334-3234
02-302-3033
010-1321-4043
02-01-32
33-3303-3033
016-444-3042
"""

#가운데 번호가 3개 ~ 4개 
reg = "[0-9]{3}-[0-9]{3,4}-[0-9]{4}"
results = re.finditer(reg ,numbers)

for result in results:
    print(result.group())
    print(result.start())
    print(result.end())
    print(result.span())

print(re.sub(reg," ",numbers))