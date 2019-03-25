class Sam(object):
    def __init__(self, num):
        self._num = num

    def __add__(self, other):
        return self._num + other._num

    def __divmod__(self, other):
        mok = self._num // other._num
        nam = self._num % other._num
        return mok, nam

s1 = Sam(7)
s2 = Sam(3)
# num = s1 + s2
num = divmod(7, 3)
num = divmod(s1, s2)
print(num)
