#Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

veh_1 = Vehicle(200, 2000)
veh_2 = Vehicle(250, 6000)

print(veh_1.max_speed, veh_1.mileage)
print(veh_2.max_speed, veh_2.mileage)