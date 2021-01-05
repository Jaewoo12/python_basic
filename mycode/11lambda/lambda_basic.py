def add(x, y):
    return x + y

print(add(10,20))

add2 = lambda x, y: x+y
print(add2(10,20))

print((lambda x, y: x+y)(10, 20))

print((lambda x: x** 2) (10))

#1 map(함수, list) 함수
double_val = lambda x: x**2
print(double_val(2))

#2 for loop 사용해서 함수호출
my_list = [1, 2, 3, 4, 5]
result_list = []
for val in my_list:
    print(double_val(val))
    result_list.append(double_val(val))
print(result_list)

#2 for loop 함수 하지않고!
result = map(double_val,my_list)
print(type(result), result) #map은 객체로 보여줌 그러므로 list 써야됨

result = list(map(double_val,my_list))
print(type(result),result)

#2 my_list를 순회(iterate) 하면서 값을 제곱값을 변환하는 함수를 호출
result = list(map(lambda x: x ** 2,my_list))
print(result)

#3 [1,2,3,4,5], [10,20,30,40,50] 두개의 리스트의 값을 더하기
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [10, 20, 30, 40, 50]
add1 = lambda x, y: x + y
result = list(map(add1, my_list, my_list2))
print(result)

result = list(map(lambda x, y: x + y, my_list, my_list2))
print(result)

#3 짝수만 제곱하는 함수
double_even = lambda x: x ** 2 if x % 2 == 0 else x
print(double_even(4),double_even(5))
print(list(map(double_even,my_list1)))
print(list(map(lambda x: x ** 2 if x % 2 == 0 else x , my_list1)))

print('map', map(double_even,my_list1))
for val in map(double_even, my_list1):
    print(val)

map_obj = map(double_val, my_list1)
print(next(map_obj),next(map_obj))

# reduce() 함수

from functools import reduce

add2 = lambda x, y: x + y
print(add2(10,20))

result = reduce(add2, my_list1)
print(result)
result = reduce(lambda perv, curr: perv + curr, my_list1)
print(result)

result_str = reduce(lambda perv, curr: perv + curr, ['aa','bb','cc'])
print(result_str)

# filter() 함수
my_len = lambda my_str: len(my_str) >6

print(my_len('hello'), my_len('mypython'))

# 6글자 이상인 문자열만 리스트에 저장하기
my_list_str = ['hello', 'mypython', 'Machine', 'Deep', 'DataScience']
result = filter(my_len, my_list_str)
print(result)        # 결과 객체로 나옴
print(list(result))  # 결과 보고싶으면 list로! map처럼
