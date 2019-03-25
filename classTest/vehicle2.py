class Truck:
    def __init__(self):
        self._speed = 0

    def get_speed(self):
        return self._speed

    def start(self):
        self._speed = 10

    def accelerate(self):
        self._speed = self._speed + 20

    def stop(self):
        self._speed = 0
