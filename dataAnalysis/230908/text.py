import requests,re
from bs4 import BeautifulSoup

text= ""

reg = "[0-9,]+원"
re.finditer(reg, text)