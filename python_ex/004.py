sum = 0

for i in range(5):
    sum = sum + int(input("값을 입력해주세요"))
    #sum += int(input("값을 입력해주세요"))

print(f'합계 : {sum}, 평균 : {sum/5}')