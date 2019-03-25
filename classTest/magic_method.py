class Car(object):
    def __init__(self, name):
        self._name = name
    def __str__(self):
        return "Type: Car, Name: " + self._name
    def __repr__(self):
        return "Car('" + self._name + "')"

if __name__ == "__main__":
    my_car = Car("Sonata")               
    my_car_string = str(my_car)          
    print(my_car_string)                 
    print(my_car)
    my_car_repr = repr(my_car)           
    print(my_car_repr)                    
    my_car1 = eval(my_car_repr)           
    print(isinstance(my_car, Car))    # Car 클래스 객체로 만들어졌는가?
    print(my_car is my_car1)          # 같은 객체인가
