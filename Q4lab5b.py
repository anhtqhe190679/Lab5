#phan1
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus('School Volvo', 12, 50)
print(type(School_bus))
#phan2
if isinstance(School_bus, Vehicle):
    print('True')
else:
    print('False')