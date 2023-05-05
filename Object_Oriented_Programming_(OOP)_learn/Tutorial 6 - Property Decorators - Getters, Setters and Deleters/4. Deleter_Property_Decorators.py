#What is the Deleter Property Decorator?
#Implemented using '@<property-name>.deleter', it specifies the delete method as a property that deletes 
#a property.

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

    @fullname.setter                #This is the Setter Property Decorator
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    #This is how we implement a Deleter Property Decorator. Similar to the Setter Property Decorator,
    #first we put in the property's name that we want to set, and then a '.deleter' function behind (what
    #we want to set is described below in the main code)

    @fullname.deleter               #This is the Deleter Property Decorator
    def fullname(self):
        #Prints this to at least show an output as evidence that this Delete Property Decorator has ran
        print('Deleting Object...')
        del self.first
        del self.last
        del self.pay
        #According the Corey Schaufer's video, he chose to 'delete' an 'Employee' object by substituting\
        #the employee's first and last name to None, but I chose to delete them completely.
        #self.first = None
        #self.last = None

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

#Lets say you want to delete an 'Employee' object. You can do this via the Deleter Property Decorator,
#and delete the object by deleting its attributes (first, last and pay)

#This is how you use the Deleter Property Decorator's method. When you run this line of code, the code
#under the Deleter Property Decorator will run and delete the 'Employee' object's attributes (effectively
#deleting the 'Employee' object)
del emp_1.fullname

#When you try to run the 'Employee' object via any of its attributes, it will return you an error, saying
#it no longer exists
print(emp_1.fullname)