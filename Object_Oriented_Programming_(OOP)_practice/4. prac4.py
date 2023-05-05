#Exercise 4: Class Inheritance
#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of 
#Bus.seating_capacity() a default value of 50.

#Expected Output:
#The seating capacity of a bus is 50 passengers

#Given:
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

#Continued:
class Bus(Vehicle):

#    def seating_capacity(self, capacity=50):
#        return f"The seating capacity of a {self.name} is {capacity} passengers"

    #Answer is a little better as their code is less repetitive, making use of the 'super()' function to
    #link the Class method in the parent class to this SubClass as the same return value as the 
    #'seating_capacity()' method in the parent Class in the 'seating_capacity()' method in this SubClass
    def seating_capacity(self):
        return super().seating_capacity(capacity=50)

veh_1 = Vehicle('Ferrari', 200, 2000)
bus_1 = Bus('School Volvo', 180, 12)

#I think you don't have worry of the wrong 'seating_capacity()' method called (cuz there's 2, one in the
#'Vehicle' parent Class, the other in the 'Bus' SubClass) When this method is called here I believe
#Python will first check within the Class (Bus) object for such a method, and only if it is not present
#then it'll check the parent Class (Method Resolution Order thing)
print(bus_1.seating_capacity())