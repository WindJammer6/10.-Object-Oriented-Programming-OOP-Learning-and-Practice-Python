#Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle 
#class

#Expected Output:
#Vehicle Name: School Volvo Speed: 180 Mileage: 12

#Given:
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

#Continued:
class Bus(Vehicle):
    pass

bus_1 = Bus('School Volvo', 180, 12)

print('Vehicle Name:', bus_1.name, 'Speed:', bus_1.max_speed, 'Mileage:', bus_1.mileage)