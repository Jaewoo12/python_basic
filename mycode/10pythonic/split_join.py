# split과 join 함수
# split은 str을 list로 .
# join은 list를 str로

my_str = 'java python kotlin'
my_list = my_str.split()   # 기준안주면 디폴트값으로 빈칸
print(type(my_list),my_list)

my_str2 = ''.join(my_list)
print(my_str2)

my_str = 'java,python,kotlin'
mylist = my_str.split(',')
print(type(my_list),my_list)

my_str2 = ','.join(my_list)
print(my_str2)