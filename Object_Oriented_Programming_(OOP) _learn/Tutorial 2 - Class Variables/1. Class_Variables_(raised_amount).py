#What are Class Variables?
#Class Variables are variables that are shared among all Class Instances of a Class.
#So, while Class Instances can be unique to each other (in terms of name, email and pay in this case),
#Class Variables are the same for all Class Instances of a Class (such as the raised_amount here)

#Lets say the company's boss will be giving a raise in pay at the end of the year to all the Employees.
#The amount raised by each Employee will be the same hence we can store the value raised as a Class
#Variable.

class Employee:

    #This is where Class Variables are placed (after you pull out the 1.04 (refer to below code))
    raised_amount = 1.04

    def __init__(self, first, last, pay):       #Attributes of each Class Instance (object in a Class)
        self.first = first                      #can also be called Instance Variables 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  
    
#Here we will create the 'apply_raise(self)' method to apply the raise to the Employee's pay when
#this function is called.

#Technically you could implement this method by:
#   def apply_raise(self):
#       self.pay = int(self.pay * 1.04)

#However there is a flaw for this. You will not be able to easily access the amount raised for all the
#Employees. Hence it will be better to pull the '1.04' out and store it outside the method, but still
#within the Class, in a variable called the Class Variable, so you can easily access it.

#Also, take note of the 'self' in 'self.raised_amount'. This placeholder MUST be filled as you will get 
#a name error if you left it as 'raised_amount'. This is because when you access a Class Variable, you 
#need access it either through the Class (Employee.raised_amount), or the Class Instance 
#(self.raised_amount). They both work, but with some differences. 

#The difference is:
#-> When you access it via the Class (Employee), when this method is called in the main code it immediately
#   checks the Class Variables, without checking the Instance Variables hence it is locked and the amount
#   raised cannot be changed for a specific Class Instance and is fully fixed to be the same for all Class
#   Instances (unless the Class Variable itself is changed)
#-> When you access it via the Class Variable (self), it gives you more flexibility as you can change the
#   amount raised of a specific Class Variable. In the main code when you access it via Class Instance,
#   and the method is called, it first checks the Instance Variable/Attributes first, which btw does not 
#   appear (you can check with the print('emp_1.__dict__' function)), hence it checks the Class where the
#   Class Instance is from for the Class Variables where it finds the 'raised_amount' variable. You can
#   change a specific Class Instance's raised amount by introducing an Instance Variable 'raised_amount'
#   and since by accessing the 'raised_amount' variable by the Class Instance, it first checks the 
#   Instance Variables before the Class Variables, and since it found the Instance Variable's
#   'raised_amount' first it will treat that as the 'raised_amount' to pass through the 'apply_raise(self)'
#   method instead, ignoring the Class Variable's 'raised amount'.

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#As you can see before the raise, employee 2 is paid 60000, after the raise of 1.04, employee 1 is paid
#62400
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

#Changing employee 1's raised amount, and checking the different attributes and methods (for Classes)
#in the 'Employee' Class, employee 1 and employee 2 Class Instances. (Notice employee 1 have 1 more
# attribute more tha employee 2 of 'raised_amount')

#Employee.raised_amount = 1.06 (also can to change raised amount of the Class (and hence its Class
#Instances) to 1.06)
emp_1.raised_amount = 1.05
print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

#Here you can see after changing employee 1's raised amount, employee 1 have raised amount of 1.05, but
#the Class Variable for 'raised_amount' and the employee 2 Class Instance's 'raised_amount' remained
#as 1.04
print(Employee.raised_amount)
print(emp_1.raised_amount)
print(emp_2.raised_amount)

#As you can see before the raise, employee 1 is paid 50000, after the raise of 1.05 (changed from 1.04 in
#1 of the previous lines of code), employee 1 is paid 52500 (5% more instead of 4% more)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)