#실습04
#사용자로부터 값을 5개 입력받아 각각 합계와 평균을 구하세요.

sum = 0
avg = 0
for i in range(0,5):
  input_num = int(input("값을 입력하세요 : "))
  sum += input_num
  
avg = sum/5
print(f'{sum}')
print(f'{avg}')
