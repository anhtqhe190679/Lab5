#phan1
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass
class Color(Vehicle):
    color = 'White'
vehicle1 = Vehicle('School Volvo', 180, 12)
vehicle2 = Vehicle('Audi', 240, 18)
print(f'{Color.color} {vehicle1.name} Speed: {vehicle1.max_speed} Mileage: {vehicle1.mileage}')
print(f'{Color.color} {vehicle2.name} Speed: {vehicle2.max_speed} Mileage: {vehicle2.mileage}')

#phan2
class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        fare = 0
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        fare = self.capacity * 100
        return fare + 1/10*(fare)
class Bus(Vehicle):
    pass

School_bus = Bus('School Volvo', 180, 12, 50) 
print(f'Total Bus fare is: {School_bus.fare()}')