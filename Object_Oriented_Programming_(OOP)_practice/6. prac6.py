#Exercise 6: Class Inheritance
#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle 
#is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a 
#maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of 
#the total fare.

#Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the
#fare() method of a Vehicle class in Bus class.

#Expected Output:
#Total Bus fare is: 5500.0

class Vehicle:

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def default_fare_charge(self):
        return self.capacity * 100

class Bus(Vehicle):

    def default_fare_charge(self):
        return super().default_fare_charge() * 1.10

veh_1 = Vehicle('Ferrari', 200, 2000, 6)
bus_1 = Bus('School Volvo', 180, 12, 50)

print(f"Total Vehicle fare is: {veh_1.default_fare_charge()}")
print(f"Total Bus fare is: {bus_1.default_fare_charge()}")

