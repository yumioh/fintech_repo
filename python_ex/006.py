#x = [2, 5, 7, 5, 8, 3, 6, 7, 3, 3, 7, 8, 9, 10, 2]
#위의 리스트를 선언하여 for 문을활용 숫자가 3이거나 
#“ 숫자가 3입니다. ” 숫자가 7일경우 “ 숫자가 7입니다. “ 
# 아닐경우 그냥 숫자가 출력되도록 만들어주세요.

x = [2, 5, 7, 5, 8, 3, 6, 7, 3, 3, 7, 8, 9, 10, 2]

for number in x:
  if number == 3:
    print("숫자가 3입니다")
  if number == 7:
    print("숫자가 7입니다")
  else :
    print(number)
