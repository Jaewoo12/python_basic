#dict 타입
#dict (), {}

lang_dict = {}
lang_dict2 = dict()
print(type(lang_dict), type(lang_dict2))

# dict에 값을 지정
lang_dict[100] = '자바'
lang_dict[200] = '파이썬'
lang_dict[200] = '텐서플로'
lang_dict[300] = '파이토치'

print(lang_dict)

# dict에서 값을 읽기
print(lang_dict[300])
value = lang_dict.get(400)
print(value)
if value:
    print(value)
else:
    print('해당 key 값이 없습니다')

for k, v in lang_dict.items():
    print(k, v)

print('자바' in lang_dict.values()) # 값으로 찾으려면 .values() 써야됨 아니면 무조건 키로 찾음

# zip() 함수
days = [ '월요일' , '화요일', '수요일', '목요일']
fruits = ['사과', '바나나', '딸기']
coffees = [ '아메리카노', '라떼', '모카', '믹스']

print(zip(days, fruits, coffees), type(zip(days, fruits, coffees)))
for day, fruit, coffee in zip(days, fruits, coffees):
    print(day, fruit, coffee)

print(dict(zip(days, fruits)))
print(list(zip(days, coffees)))

for value in list(zip(days, coffees)):
    print(value)

days_tuple = '월요일', '화요일', '수요일' #() 안줘도 알아서 튜플로됨

# zip(), range() 함수는 iterable 객체를 반환하기 때문에 값을 확인하려면 for in / list()와 함께 써야된다
print(range(10))
print(list(range(1,10,2)))


