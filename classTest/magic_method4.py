class Sam(object):
    def __init__(self, num):
        self._num = num

    # def __eq__(self, other):
    #     return self._num == other._num

    def __bool__(self):
        return self._num > 5
s1 = Sam(7)
s2 = Sam(3)
s3 = Sam(7)
print(s1 == s3)
if s2:
    print("크다")
else:
    print("작다")
