#What are Static Methods?
#-> Instance Methods are functions in a Class that takes in Class Instances as its first parameter as
#   'self' by convention
#-> Class Methods are functions in a Class that takes in Classes as its first parameter as
#   'cls' by convention
#-> Static Methods are functions in a Class that takes in neither Classes or Class Instances as its first 
#   parameter. You just pass in whatever else parameters/arguments that you need for the method to work

#Hence if you think about it, Static Methods behave exactly like regular functions, but you would want to
#put it under the 'Employee' Class because it has some logical connection to the Class

import datetime

class Employee:

    number_of_employees = 0
    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

    @classmethod
    def from_string(cls, hyphened_employee_info):
        first, last, pay = hyphened_employee_info.split('-')
        return cls(first, last, pay)
    
    #This is how we implement a Static Method, by first adding the @staticmethod decorator (theres other
    #types of decorators in Python). Notice that for static methods, it takes in neither Classes
    #or Class Instances as the first parameter, and just jump straight to the relevant parameters (day)

    #Now, a foolproof method to check if a method is supposed to be Static, instead of Class or Class
    #Instance, you can just check if within the method is there a need to call for access to a Class/
    #Class Instance. If there is no need then it will be a Static Method, and no need to pass any
    #Class (cls) or Class Instance (self) as the first parameter
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:          #'.weekday()' is a Python function (not a
            return False                                      #datetime module function!) that takes in
        return True                                           #a date from the datetime module and returns
                                                              #a number from 0 to 6 (0 as Monday, 6 as
                                                              #Sunday, can see documentation)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#This is how you run the Static Method from the 'Employee' Class in the main code
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))



