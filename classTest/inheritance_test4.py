# 사람과 학생 클래스 관리
class Person(object):
    def __init__(self, name='abc', age=1):
        self._name = name
        self._age = age


class Student(object):
    def __init__(self):
        self._name = '홍길도'
        self._age = 25
        self._depart = 'python'


class Student1(Person):
    def __init__(self, name='abc', age=1, depart='python'):
        super().__init__(name, age)
        self._depart = depart


# s = Student1('hadoop')
s = Student1('kim', '24', 'hadoop')
s1 = Student1()

print(s._depart, s._name, s._age)
print(s1._depart, s1._name, s1._age)


