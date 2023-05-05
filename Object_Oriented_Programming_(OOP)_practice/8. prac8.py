#Exercise 8: Determine if School_bus is also an instance of the Vehicle class

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

#Output for this line of code is True, hence the 'Bus' object, 'School_bus' is an instance of the
#'Vehicle' Class
print(isinstance(School_bus, Vehicle))