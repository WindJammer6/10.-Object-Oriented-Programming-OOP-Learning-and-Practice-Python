#What is the Setter Property Decorator?
#Implemented using '@<property-name>.setter', it specifies the setter method for a property that sets the
#value to a property.

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property                       #This is the Getter Property Decorator
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)  

    @property                       #This is the Getter Property Decorator
    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
    #This is how we implement a Setter Property Decorator. First we put in the property's name that
    #we want to set, and then a '.setter' function behind (what we want to set is described below in
    #the main code)

    @fullname.setter                #This is the Setter Property Decorator
    def fullname(self, name):
        #Splitting the provided string into 2 strings at the spacing, and storing the first string as
        #the 'Employee' object's 'first' name and last string as 'Employee' object's 'last'name.
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#Lets say we also want to be able to change the attributes of an employee by changing its full name.
#We also want, by changing the 'Employee' object's full name, also change its first, last and email.
#Hence this is when the Setter Property Decorator can solve our problem.
emp_1.fullname = 'John Smith'

#To check if the Setter Property Decorator works and if the 'Employee' object's first name, last name
#and emails have been changed
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)