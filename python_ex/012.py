number_list = []

for i in range(10):
    number = int(input("값을입력해주세요"))

    if number == 0:
        number_list.append(number)
    elif number % 2 == 0:
        number_list.append('짝수')
    else:
        number_list.append('홀수')

print(number_list)