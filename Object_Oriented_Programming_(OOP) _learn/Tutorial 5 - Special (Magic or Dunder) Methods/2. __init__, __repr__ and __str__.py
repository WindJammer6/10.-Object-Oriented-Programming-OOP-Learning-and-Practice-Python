#About __init__.
#From the past tutorials we have already been using the '__init__' Special Method which is called whenever
#a object (Class Instance) is made to provide the attributes of that object.

#Apart from the '__init__' Special Method, there are these 2 other Special Methods we should always
#implement, '__repr__' and '__str__'.

#//////////////////////////////////////////

#What is __repr__ and __str__? What are they for?
#--> In short, '__repr__' is the unambiguous representation of an object and should be used for logging 
#and debugging, it is meant to be seen by other Developers (not user friendly but it shows the true nature 
#of the object).
#--> In short, '__str__' is meant to be a more readable representation of an object and should be used as
#a display to the user (more user friendly).

#These 2 function technically already exist in Python (shown below), but lets modify/build on them such 
#that it works for our 'Employee' Class

#These code shows that the 'repr()'/'__repr__' and 'str()'/'__str__' technically already exists in Python.
#Both will show the same thing without implementing these Special Methods in our Class (will be explained
#why in the code below), a hard-to-read output of the object Class and memory address 
#'<__main__.Employee object at 0x000001919D0E7AD0>'. 
#   print(repr(emp_1))
#   print(str(emp_1))
#   print(emp_1.__repr__())
#   print(emp_1.__str__())

#So we want to change this by implementing these Special Methods in our Class, which will be shown how
#below.

class Employee:

    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    #If you only create a '__repr__(self)' Special Method without creating a '__str__(self)' Special Method,
    #if you call an 'Employee' object using '__str__(self)' it will fallback to your '__repr__(self)'
    #method and return whatever you put under '__repr__(self)' hence its advised for you to have both
    #'__repr__(self)' and '__str__(self)' not omit either.

    #It is advised that you return something in your '__repr__(self)' that you can just copy paste back into
    #your code to recreate that exact same object
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)   #Apparently if you want
                                                                                    #add quotation marks
                                                                                    #within quotation marks
                                                                                    #you need to have "" as
                                                                                    #the outside quotation
                                                                                    #and '' as the inside or
                                                                                    #the code won't work
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#This shows that the '__repr__(self)' Special Method works. Without the '__repr__(self)' Special Method
#these would have printed '<__main__.Employee object at 0x000001919D0E7AD0>', but now it prints what
#specified to returned in our '__repr__(self)' Special Method, 'Employee('Corey', 'Schafer', 50000)'

#Notice that 'Employee('Corey', 'Schafer', 50000)' is literally how we would create our Employee 
#object, which we are advised to return in our '__repr__(self)' Special Methods.
print(emp_1.__repr__())
print(repr(emp_1))

#This shows that the '__str__(self)' Special Method works. Without the '__str__(self)' Special Method
#these would have printed '<__main__.Employee object at 0x000001919D0E7AD0>', but now it prints what
#specified to returned in our '__str__(self)' Special Method, 'Corey Schafer - Corey.Schafer@company.com'
print(emp_1.__str__())
print(str(emp_1))

#Notice for this one, it prints out what was stated to be returned in the '__str__(self)' Special Method.
#(Corey Schafer - Corey.Schafer@company.com) If without the '__str__(self)' Special Method, it will 
#fallback to print what was stated to be returned in the '__repr__(self)' Special Method instead (as 
#commented up in the '__repr__(self)' Special Method code), unless otherwise instructed using the 
#'__repr__' or 'repr()' function.
print(emp_1)

