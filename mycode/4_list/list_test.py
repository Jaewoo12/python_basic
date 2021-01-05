'''
list 타입을 선언하고 list에 엘리먼트 추가,삭제
'''
num_list = [60 ,10, 20, 40, 50, 30, ]
num_list2 = [1, 2, 3, 4, 5]
# 리스트의 메모리 저장 방식
print(num_list, num_list2)
num_list2 = num_list
print(num_list, num_list2)
num_list.sort()
print(num_list, num_list2)
num_list2 = [1, 2, 3, 4, 5]
num_list.sort()
print(num_list, num_list2)

print(type(num_list),num_list)
print(num_list[0], num_list[0:3], num_list[3:])
for num in num_list:
    print(num)

for idx, num in enumerate(num_list):
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
print(type(str_list), str_list)

# index로 list의 엘리먼트(혹은 아이템) 값을 변경
str_list[1]= 'java script'
print(str_list[1], str_list[2:4])

# 엘리먼트 추가
str_list.append('Cobol')
print(str_list)

# 엘리먼트 중간에 추가
str_list.insert(1, 'type script')
print(str_list)

for idx, val in enumerate(str_list):
    print(idx,val)

mix_list = [100, 3.14 , True , '파이썬']
for mix in mix_list:
    print(type(mix),mix)

#엘리먼트 삭제

str_list.remove('Cobol') #값으로삭제
del str_list[0]
del str_list[:3]
print(str_list *2 )
print('Scalar' in str_list)
print('java' in str_list)

my_list = list('Python')
print(type(my_list), my_list)

my_list2 = 'Hello, Python'.split(',') #str -> list
print(my_list2)

# packing
my_list3 = ['aa', 'bb', 'bb', 'ab']  #여러개 값을 하나의 변수에 넣겠다(packing)
print(my_list3.index('bb'))
print(my_list3.count('bb'))

#unpacking
str1, str2 = ['cc', 'dd']
print(str1)
print(str2)

