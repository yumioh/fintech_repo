#위와같이 사용자로부터 점수 3개를 입력받아 입력받은 값의 평균이
# 50을 넘으면 합격 아니면 불합격을 출력해주세요. 
#단, 30점을 넘지 못하는 과목이 있으면 무조건 불합격을 출력해주세요.

# one = int(input("첫번째 점수 : "))
# two = int(input("두번째 점수 : "))
# three = int(input("세번째 점수 : "))

avg = 0
sum = 0

# sum = input_one + input_two + input_three
# avg = sum/3

number = 0

for i in range(3):
  number += int(input("값을 입력해주세요 : "))
  if number < 30 or number < 30 or number < 30:
      ("불합격")
  elif avg > 50:
     print("합격")
  else : 
      print("불합격")
