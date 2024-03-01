class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
vehicle = Vehicle('School Volvo', 180, 12)
print(f'Vehicle Name: {vehicle.name}, Speed: {vehicle.max_speed}, Mileage: {vehicle.mileage}')


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity=50):
        return f'The seating capacity of a {vehicle.name} is {capacity} passengers'
bus = Bus('School Volvo', 180, 12)
print(bus.seating_capacity())


    
    
   
    
    