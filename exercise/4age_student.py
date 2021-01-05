'''
#나이 = 현재년도 - 태어난 년도 + 1
#태어난 년도를 입력받음 input()

from 모듈명 import
'''

from datetime import datetime as dt
#현재년도 datetime 클래스에 선언된 today() 메서드를 호출
current_year = dt.today().year

print('태어난년도 입력하시오')
input_year = int(input('태어난 년도를 입력하세요'))
age = current_year - input_year + 1
print(input_year, age)

if 17 <=age <20:
    print('고등학생')
elif (age >= 20) and (age <= 27):
    print('대학생')
else:
    print('학생이 아닙니다')