class A:
    def pr(self):
        print('A')


# 오버라이딩, 재정의 되었다.
class SubA1(A):
    def pr(self):
        print('pr1')


class SubA2(A):
    # def pr(self):
    #     print('pr2')
    pass


class SubA3:
    #print('Suba3')
    pass


class MyApp(A):
    def pr(self):
        self.my_print()

    def my_print(self):
        print('my print')

    def fff(self):
        self.my_print()
        self.my_print()


def f(ss):
    if isinstance(ss, A):
        ss.pr()
    else:
        print('다른 객체 입니다')
    pass


s = SubA1()
s2 = SubA2()
s.pr()
s2.pr()
print('---------------')

a = A()
s3 = SubA3()
myapp = MyApp()

f(a)
f('korea')
f(s3)
f(myapp)


