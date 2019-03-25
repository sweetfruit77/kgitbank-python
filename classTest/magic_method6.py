class Student:
    def __init__(self, name, jumsu=0):
        self._name = name
        self._jumsu = jumsu

    def __add__(self, other):
        if isinstance(other, Student):
            return self._jumsu + other._jumsu
        else:
            print('Student 타입만 가능 합니다.')
            return 0

    def __repr__(self):
        return '이름 {}, 점수 {}'.format(self._name, self._jumsu)


s1 = Student('홍길동', 78)
s2 = Student('장나라', 32)

tot = s1 + s2
print(tot)
tot = s1 + 'kroea'
print(tot)

