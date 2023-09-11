# For문을 사용하여 사용자에게 3명의 학생정보를 입력받아
# 총 3개의 딕셔너리가 들어있는 리스트를 만들어주세요.

dic_users = []
for i in range(0, 3):
    name = input("이름 입력 :")
    gender = input("성별 입력 :")
    age = input("나이 입력 :")
    dic_user = {"name": name, "gender": gender, "age": age}
    dic_users.append(dic_user)
print(dic_users)
