"""def change(a):
    return float(((9 / 5) * a) + 32)

print('본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.')
print('변환하고 싶은 섭씨 온도를 입력해주세요')
a = float(input())

print('화씨온도', a)
print('섭씨온도', (round(change(a),2)))"""


# 강사님이 한 코드

def fah_convert(value):
    #fah = ((9/5) * float(user_input))+32
    return ((9/5) * float(value) + 32)

def sayHello(msg):
    return f'Hello {msg}'

