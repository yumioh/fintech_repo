# 리스트는 같은 성격의 데이터를 넣는 경우가 많음
# 딕션너리는 다른 성격의 데이터를 넣는 경우가 많음

numbers = [1,232,525,'adfs',[12,23,22,55]]

for idx,val in enumerate(numbers):
    numbers[idx] = 0
# print(numbers)

print(numbers[0][2])

a = {
    'name':'홍길동',
    'age' : 24,
    'address' : [12,325,665,25]
}

#for인 경우 key값이 출력
#dict 변수명[키값] -> value 출력
for val in a:
    a[val] = 0
print(a)



