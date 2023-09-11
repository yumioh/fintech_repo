a = 213123
a = 131.23223
a = False
a = None
a = 'djdjdjdjdj'
#          0     1        2          3              4
numbers = [1, 322.3232, 343434, 'sdfsfdsfsd', [12,23,23,223]]
numbers[1] = 2
#numbers.append(3)
#numbers.insert(1, 3)
#numbers.pop()
#print(numbers)
numbers[4][3] = 0
#print(numbers)


a = {
        'name':'이진범',
        'age': 38,
        'address': [1,2,3, 232 ,32, 32]
    }
a['age'] = 40
#print(a['address'][3])


#         0       1       2          3              4
numbers = [1, 322.3232, 343434, 'sdfsfdsfsd', [12,23,23,223]]

# numbers[0] = 0
# numbers[1] = 0
# numbers[2] = 0
# numbers[3] = 0
# numbers[4] = 0

for idx, value in enumerate(numbers):
    numbers[idx] = 0

#print(numbers)

a = {
    'name':'이진범',
    'age': 38,
    'address': [1,2,3, 232 ,32, 32]
}

for value in a:
    a[value] = 0

print(a)

