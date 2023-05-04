#What are Class Methods?
#-> Up until now, we have been creating Instance (Regular) Methods, which takes in the Class Instance as the
#   first parameter as 'self'. 
#-> What if we want to alter the functionality of the method, to take in the Class as the first parameter 
#   instead of the Class Instance? 
#   We will be demonstrating how to do this below. When a method takes in the Class as the first parameter, 
#   it is now called a Class Method instead.

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

    #This is how we implement a Class Method, by first adding the @classmethod decorator (theres other
    #types of decorators in Python). Now instead of taking a Class Instance (self) as the first parameter,
    #it takes a Class (cls) as the first parameter.

    #Like how 'self' is a convention to indicate the Instance method taking a Class Instance as the first
    #parameter/argument, 'cls' is the convention placeholder to indicate the Class method taking a Class
    #as the first parameter
    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#This is how you use the Class Method in the main code. It actually does the same thing as:
#   Employee.raised_amount = 1.05
#But you are doing it through a Class Method instead

#Now, you can actually also run the Class Method in the main code through a Class Instance but it does
#not make a whole lot of sense and people usually don't do it. This is how it looks like:
#   emp_1.set_raised_amt(1.05)
#It works exactly the same as running the Class Method through a Class (changing the 'raised_amount' of 
#the Class instead of a specific Class Instance like you'd expect but no). You can check by printing out
#the 'raised_amount' of the Class and the respective Class Instances, you'll get the same for all.
Employee.set_raised_amt(1.05)

print(Employee.raised_amount)
print(emp_1.raised_amount)
print(emp_2.raised_amount)

print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)