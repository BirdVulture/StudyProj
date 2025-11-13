class Vehicle:
    vehicles_created = 0
    
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        Vehicle.vehicles_created = Vehicle.vehicles_created + 1
        
    def get_max_speed(self):
        return self._max_speed
        
    def get_mileage(self):
        return self._mileage
        
    def drive(self, distance):
        self._mileage = self._mileage + distance
            
    def display_info(self):
        print(f"""Марка: {self.brand}\nМакс. скорость: {self._max_speed} км/ч\nПробег: {self._mileage} км""")

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

v1 = Vehicle("Tesla", 100)

print(v1.get_max_speed())
print(v1.display_info())