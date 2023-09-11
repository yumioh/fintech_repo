number1 = int(input("값을 입력해주세요"))
number2 = int(input("값을 입력해주세요"))
number3 = int(input("값을 입력해주세요"))

average = (number1 + number2 + number3) / 3

if number1 < 30 or number2 < 30 or number3 < 30:
    print('불합격')
elif average > 50:
    print('합격')
else:
    print('불합격')