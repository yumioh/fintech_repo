#x = [2, 5, 7, 5, 8, 3, 4, 5, 7]
#위의 리스트를 선언하고 숫자가 3이거나 
#숫자가 7인숫자를 0으로 바꿔 출력해주세요

x = [2, 5, 7, 5, 8, 3, 4, 5, 7]

#리스트의 값을 바꿀려면 index값을 찾아서 값을 바꿔야함
#for idx, val in enumerate(x):
#   if val == 3 or val == 7

for i in range(len(x)):
  if x[i] == 3:
    x[i] = 0
  if x[i] == 7:
    x[i] = 0
  else:
    x
print(list(x))