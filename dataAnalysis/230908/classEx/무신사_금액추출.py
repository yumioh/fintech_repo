import re
from bs4 import BeautifulSoup

text = """
<p class="box_price">
<span class="txt_origin_price">75,000원</span>
71,250원
</p>
"""

bs = BeautifulSoup(text, 'html.parser')

print(bs.select_one('.box_price').text.split('원'))
print(bs.select_one('.box_price').text)

for price in re.finditer('[0-9,]+원',bs.select_one('.box_price').text):
    print(price.group())

for price in re.finditer('[0-9,]+원',str(bs.select_one('.box_price'))):
    print(price.group())