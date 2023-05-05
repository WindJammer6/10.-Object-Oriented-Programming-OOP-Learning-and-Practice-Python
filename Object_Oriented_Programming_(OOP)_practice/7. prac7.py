#Exercise 7: Check type of an object
#Write a program to determine which class a given Bus object belongs to.

#Given:
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

#Continued:
veh_1 = Vehicle('Ferrari', 200, 6)
School_bus = Bus("School Volvo", 12, 50)

print(type(veh_1))
print(type(School_bus))