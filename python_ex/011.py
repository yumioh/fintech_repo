#FOR 문을 이용 사용자에게 총 10개의 숫자를 입력받아 
#입력받은수가 
#짝수일경우 짝수, 홀수일경우 홀수, 
#0을 입력할경우 0이 들어가있는 총 10개짜리 리스트를 만들어주세요

list_num = []
for i in range(0,10):
  input_num = int(input("숫자를 입력해 주세요 : "))

  if input_num == 0:
    list_num.append(0)
  elif input_num %2 == 0:
    list_num.append("짝수")
  else:
    list_num.append("홀수")
print(list_num)