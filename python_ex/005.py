#사용자로부터 값을 5개 입력받아 리스트로 만들어주세요.

num_list = []
for i in range(5):
  input_num = int(input("값을 입력하세요 : "))
  num_list.append(input_num) # list에 값 추가 append 사용
print(num_list)