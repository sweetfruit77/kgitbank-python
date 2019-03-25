class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getName(self):
        print('get name')
        return self._name

    def setName(self, name):
        if name == '장나라':
            print('{} 이름은 변경 불가 합니다'.format(name))
            return
        print('set name', name)
        self._name = name

    # 프로퍼티 구현 방법!!!
    name = property(getName, setName)

    def getAge(self):
        return self._age

    def setAge(self, age):
        if age < 1:
            print('0 보다 작은 나이는 입력불가 합니다.')
            return
        self._age = age

    #age = property(getAge, setAge)    


p2 = Person2('홍길동', 20)
print(p2.name)
p2.name = '장나라'
print(p2.name)

#print(p2.age)

