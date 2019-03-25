class Person1:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def speed(self, value):
        self._age = value


p1 = Person1('홍길동', 20)
print(p1.name)
p1.name = '장나라'
print(p1.name)