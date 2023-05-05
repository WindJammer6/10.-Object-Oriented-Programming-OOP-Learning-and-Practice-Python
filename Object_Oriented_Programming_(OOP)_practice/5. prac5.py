#Exercise 5: Define a property that must have the same value for every class instance (object)
#Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
#Add an empty 'Bus' and 'Car' SubClasses of the 'Vehicle' Class.

#Expected Output:
#Color: White Vehicle name: School Volvo Speed: 180 Mileage: 12
#Color: White Vehicle name: Audi Q5 Speed: 240 Mileage: 18

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'White'

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus_1 = Bus('School Volvo', 180, 12)
car_1 = Car('Audi Q5', 240, 18)

print('Color:', bus_1.color, 'Vehicle Name:', bus_1.name, 'Speed:', bus_1.max_speed, 'Mileage:', bus_1.mileage)
print('Color:', car_1.color, 'Vehicle Name:', car_1.name, 'Speed:', car_1.max_speed, 'Mileage:', car_1.mileage)