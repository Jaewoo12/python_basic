# 키워드 파라미터
def connect(server,port):
    url = f'http://{server}:{port}'
    return url

print(connect('localhost','8080'))
print(connect(port='80',server='aa.com'))
print(connect('naver.com',port='8090'))

# arguement default value
def add(a=10, b=20):
    return a + b

print(add(40,50))
print(add())
print(add(100))
print(add(b=100))

# 가변(파라미터의 갯수가 정해지지 않음) 파ㅏㄹ미터 - tuple 타입
def kwargs_test(a, b, *p):
    print(type(p))
    print(a, b, p)
    return a + b +sum(p)

print(kwargs_test(10,20))
print(kwargs_test(10, 20, 30, 40))

# 가변 파라미터 - dict 타입
def kwargs_dict(**p):
    print(p, type(p))
    for k,v in p.items():
        print(k,v)

kwargs_dict(a=100, b=300, c=400)

# 값을 여러개 반환할수 있다 - tuple 타입으로
def swap(a,b):
    return b,a

result = swap(10,20)
print(result,type(result))

x, y = swap(10,20)
print(f'x= {x} y= {y}')