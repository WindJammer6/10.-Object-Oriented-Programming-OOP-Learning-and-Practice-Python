#What are Class Inheritance and SubClasses?
#-> Class Inheritance means when a SubClass inherit attributes and methods from a parent class. This is
#   useful because we can create SubClasses that has the functionality of its parent class and we can
#   override or add new functionalities into these SubClasses without affecting the parent class in
#   any way
#-> SubClasses are derived Classes from a parent class (called SuperClass)

#Lets say we want to create different types of employees such as Developers and Managers. They are still
#employees (with the first, last, pay, and email attributes), but of a specific kind. A logical way to 
#create the Developer and Manager objects is as SubClasses of the 'Employee' Class. (so we don't have to 
#recreate a complete different Class with the same attributes and we can just reuse/inherit the code in the 
#'Employee' Class)
class Employee:

    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

#This is how you create a SubClass, similar to a normal Class, but you add a parenthesis with the
#class you want to inherit inside. (Btw Python allows multiple inheritance (inheriting from multiple
#parent Classes))

#If you left this SubClass empty by just having a 'pass' function, it will still have (after
#inheriting from its parent Class) all the attributes and methods from its parent Class.
class Developer(Employee):
    pass

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#What is Method Resolution Order?
#When we create a 'Developer' object, 
#1. Python first searches the 'Developer' SubClass for attributes for creating the object (the '__init__'
#   method), which it finds nothing.
#2. Next, Python searches its parent 'Employee' Class for attributes for creating the object, which it
#   does.
#3. In the case there is also no attributes to be found in the 'Employee' object, the last place
#   Python will look is 'builtins.object', which is a Python Class that every other Class created inherits
#   from 
#This chain of inheritance (to find attributes/methods of an object created) is called the Method
#Resolution Order (You can see all of this and more about the 'Developer' SubClass using the 'help()' 
#function)
dev_1 = Developer('John', 'Doe', 50000)
dev_2 = Developer('Jane', 'Smith', 60000)
print(dev_1.email)
print(dev_2.email)

print(help(Developer))


