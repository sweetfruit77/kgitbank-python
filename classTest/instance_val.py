class STest:
    age = 10

s1 = STest()
s2 = STest()
s1.age = 30
s2.age = 50
s2.gender = '남'
print(s2.gender)
#print(s1.gender)
print(s1.age)
print(s2.age)
print(STest.age)
print(STest.age)
