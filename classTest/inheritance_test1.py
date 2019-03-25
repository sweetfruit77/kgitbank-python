class My:
    def __init__(self):
        self._name = "korea"
        print("My")

    def get_name(self):
        print("self._name", self._name)
        return self._name

class SubMy(My):
    def __init__(self):
        super().__init__()
        print("SubMy")
    def sub_print(self):
        print("sub_print", self.get_name())

s = SubMy()
print(s._name)
print("메소드", s.get_name())
print("-------------")
s.sub_print()
