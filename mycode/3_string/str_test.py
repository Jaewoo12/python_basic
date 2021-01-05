'''
문자열 관련 내용들
'''
# escape 문자
greet = 'hello '* 4 + '\n'
end = '\tgood \'bye\' !!'
end2 = "\t Good 'morning' ??"
print(greet + end + end2)

# bool 타입과 str 타입
is_flag = True
my_str = 'true'
my_str1 = 'false'
print(type(is_flag), type(my_str))
if is_flag:
    print(my_str)
else:
    print(my_str1)

# 문자열 인덱스(오프셋)
greeting = 'hello world'
print(len(greeting))
print('문자열 길이{}'.format(len(greeting)))
print('문자열 길이{}, 0번째 인덱스값은 {}'.format(len(greeting),greeting[0]))

# 3.6 버전 이후 생긴것
print(f'문자열 길이{len(greeting)}, 1번째 인덱스 값은 {greeting[1]}')

# c언어 스타일
print('파이썬 %s' % greeting)
print('문자열 길이 %i' %len(greeting)) # 단점은 타입을 무조건 정확하게 맞춰야됨
print('문자열 길이{}, 0번째 인덱스값은 {}'.format(len(greeting),greeting[0]))

# 문자열 인덱스 슬라이싱 [start: (end값은 exclusive )
print(f'greeting[0:5] = {greeting[0:5]}') #greeting[0:5:1]과 똑같음 .1은 default로 생략
print(f'greeting[6:11] = {greeting[6:11]}')
print(f'greeting[6:] = {greeting[6:]}')
print(f'greeting[:5] = {greeting[:5]}')
print(greeting, greeting[:])
print(greeting[::2])

# 음수값의 인덱스
print(f'greeting[-1:] = {greeting[-1:]}')

# 문자열의 역순
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 여러가지 함수들
word = 'Good manufacturing Practice Good'
print(word.upper())
result = word.upper()
print(word,'   ', result)
print(result.lower())
print(f'소문자로 변환 = {result.lower()}')
print(word.title())
print(word.find('G'))
print(word.rfind('G'))
print(word.count('d'))
word_list = word.split()
print(word_list)

word2 = 'Good/manu/facturing/Practice/Good'
print(word2.split('/'))

word3 = ' hello python '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G')) # G로시작?
print(word.endswith('G')) # G로끝남?

for val in word:
    print(val, word.count(val))

for w in word_list:
    print(w)