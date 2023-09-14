
def age_range(age):
    for i in age:
        print(i)
        if i > 70:
             return "노인"
        elif 70 > i >= 60:
            return "60대"
        elif 60 > i >= 50:
            return "50대"
        elif 50 > i >= 40:
            return "40대"
        elif 40 > i >= 30:
            return "30대"
        elif 30 > i >= 20:
            return "20대"
        elif 20 > i >= 10:
            return "10대"
        else: 
            "유아"

test =  [22, 38,38,66,77,88,99]

print(age_range(test))
