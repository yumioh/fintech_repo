# 사용자로부터 숫자를 하나 입력받아 10보다 크면 “10보다크다. 
#“ 10보다 작으면 “10보다 작다" 를 출력해주세요.

input_num =  int(input("숫자를 입력해주세요 : "))

if input_num >= 10:
  print("10보다 큽니다")
elif input_num < 10:
  print("10보다 작습니다")