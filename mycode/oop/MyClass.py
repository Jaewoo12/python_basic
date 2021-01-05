#클래스 선언
# class MyClass extends Object {} or class MyClass {} - Java
# class MyClass(object): or class MyClass: - python (object 자리엔 상속받을것쓰기)

class MyClass:
    # constructor 생성자 선언
    def __init__(self):
        # attribute(속성) 초기화
        self.num = 100
        # private 속성
        self.__name = 'dooly'

    # method(행위) 선언
    def read_number(self):
        return self.num + 100

    # 부모 클래스(object)가 가진 __str__ 메서드를 재정의 하였음
    def __str__(self):
        return f'MyClass의 속성 Num: {str(self.num)}'

    # getter method
    @property
    def name(self):
        return self.__name

    # setter method
    @name.setter
    def name(self, new_name):
        if len(new_name) == 3:
            self.__name = new_name
        else:
            print('새로운 이름의 길이는 3이어야 합니다')

# 객체를 생성
myobj1 = MyClass()
print(myobj1,type(myobj1))
#print(myobj1.__name) 이건 실행안됨
#print(myobj1.name()) 이것도 실행안됨
#getter method 호출
print(myobj1.name)
myobj1.num = 100
print(myobj1.num)

#setter method 호출
myobj1.name = '길동'
print(myobj1.name)

print(myobj1.read_number())