#숫자 3개 우선 입력받고 문자를 입력받은 다음 문자가 
#평균일경우 숫자들의 평균을 문자가 합계일때 숫자들의 합을 전체를 입력하면 
#평균과 합계가 들어있는 딕셔너리를 생성하여 출력 이외의 문자를 입력할경우 
#잘못입력하였습니다를 출력해주세요.

avg = 0
sum = 0
total = {}

num1 = int(input("첫번째 숫자를 입력해 주세요 : "))
num2 = int(input("두번째 숫자를 입력해 주세요 : "))
num3 = int(input("세번째 숫자를 입력해 주세요 : "))
cal = input("어떤 계산을 할까요?(평균, 합계, 전체) : ")
sum = num1 + num2 + num3
avg = sum/3

if cal == "합계":
  print("합계는 {}입니다".format(sum))
elif cal == "평균":
  print("평균은 {} 입니다 ".format(avg))
elif cal == "전체":
  total = {"평균":avg, "합계": sum}
  print(total)
else :
  print("잘못입력하였습니다")