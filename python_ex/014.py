number1 = int(input('숫자를입력해주세요'))
number2 = int(input('숫자를입력해주세요'))
number3 = int(input('숫자를입력해주세요'))

cal = input('어떤계산을할까요?')

sum = number1 + number2 + number3
avg = (number1 + number2 + number3) / 3

if cal == '합계':
    print('합계는', sum, '입니다.')
elif cal == '평균':
    print('평균은', avg, '입니다.')
elif cal == '전체':
    cal_dict = {
        '합계': sum,
        '평균': avg
    }
    print(cal_dict)
else:
    print('잘못입력하였습니다.')