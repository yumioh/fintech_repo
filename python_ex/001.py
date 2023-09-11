#실습01
#아래처럼 text 변수를 선언한뒤 
#replace 함수를 이용하여 자바를 -> 파이썬으로 변경하여 출력해주세요.

text = """
오늘 아침부터 저는 자바공부를 열심히 하고있습니다.
자바는 재미있습니다.
"""

text = text.replace("자바","파이썬")
test = text.replace("\n","") 
text = text.replace(" ", "")

print(text)
