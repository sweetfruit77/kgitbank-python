class Sam:
    data = "python"
    def __init__(self):
        self._data = "korea"
    def instance_method(self):
        print("instance method", self._data)
    @classmethod
    def class_method(cls):
        print("class method", cls.data)
        # print("class method", cls._data)
    @staticmethod
    def static_method():
        print("static method", Sam.data)


s = Sam()
s.instance_method()
s.class_method()
Sam.class_method()
Sam.static_method()
