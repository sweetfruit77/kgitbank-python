import random

class Dice(object):
    def __init__(self, start, end):
        print("init")
        self._start = start
        self._end = end

    def __call__(self, *args, **kwargs):
        return random.randint(self._start, self._end)


if __name__ == "__main__":
    dice = Dice(1, 6)
    
    print(dice())
    print(dice())
    print(dice())
    print(dice())
