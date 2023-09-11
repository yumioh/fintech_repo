# 가변인수 
def add_many(*agrs):
  result = 0
  for i in agrs:
    result = result + i
  return print(result)

arg_list = [1,2,3,4]
#add_many(*arg_list) # list/tuple 사용시 *변수명


def add_mul(choice, *args) :
  if choice == "add" :
    result = 0 
    for i in args:
      result = result + i
  elif choice == "mul":
    result = 1
    for i in args:
      result = result * i
  return print("선택은 : {}, 결과 : {}".format(choice,result))

arg_lists = [1,2,3,4]
add_mul("mul",*arg_lists)

#키워드 매개 변수, kwargs

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

def add_and_mul(a,b):
    return a+b,a*b

result1, result2 = add_and_mul(3,4)
print(result1, result2) ##result1 = 7 , result2=12


def say_nick(nick):
  if nick == "바보":
    return
  print("나의 별명은 %s 입니다." % nick)

say_nick("야호")

def say_myself(name, age, man=True):
  print("나의 이름은 %s 입니다." % name)
  print("나이는 %d살입니다." % age)

  if man:
    print("남자입니다")
  else:
    print("여자입니다")

say_myself("호호", 12, True)

say_myself("박응용",27)


