name = input("이름을 입력해주세요:")
math = input("수학점수를 입력해주세요:")
science = input("과학점수를 입력해주세요:")

#student = {'name':name, 'math':math, 'science':science}
student = {}
student['name'] = name
student['math'] = math
student['science'] = science

print(student)