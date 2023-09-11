students = []

for i in range(3):
    name = input("이름을 입력해주세요")
    gender = input("성별을 입력해주세요")
    age = input("나이를 입력해주세요")

    student = {
        'name':name,
        'gender':gender,
        'age':age
    }

    students.append(student)

print(students)