def phan1():
    class Vehicle:
        def __init__(self, max_speed, mileage):
            self.max_speed = max_speed
            self.mileage = mileage        
    p1 = Vehicle(240,18)
    print(p1.max_speed)
    print(p1.mileage)
def phan2():
    class Vehicle:
        pass
    car = Vehicle()

phan1()
phan2()