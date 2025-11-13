class Vehicle:
    vehicles_created = 0
    
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        vehicles_created = vehicles_created + 1

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass