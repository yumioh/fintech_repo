import re

text = "I like orange! I love orange!"
text = "orange! I love orange!"
result = re.match("orange",text)

print(result.group())
print(result.start())