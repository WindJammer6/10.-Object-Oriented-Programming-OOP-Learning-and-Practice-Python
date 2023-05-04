#In this first tutorial on OOP we will learn about Classes and Class Instances

#What are Classes and Class Instances?
#Classes are a type of object represented in code
#Class Instance is an object created from a Class. There can be multiple Class Instances created from
#a class.

#Each Class can have different attributes and methods:
#-> Attributes are characteristics of an object from the Class
#-> Methods are actions/behaviour of the object from the Class (usually done by defining functions
#   which will be associated with the Class)

#Why are Classes used?
#It is used to create a blueprint of a type of object so we don't have to re-code its attributes and
#methods everytime we want to make such an object. We can instead just refer the object to its Class and
#the object with the desired attributes and methods will be instantly created

#//////////////////////////////////

#Lets say we are making an application for a company and we want to represent employees in our Python
#code.

class Employee_:                            #If you want to leave the 'Employee_' class empty for awhile
    pass                                    #you need to enter the 'pass' function to tell Python you
                                            #want to leave it empty for now (if you leave nothing under
                                            #the 'class' function you'll get an error)

employee_1 = Employee_()                     #'employee_1' and 'employee_2' are objects created from the
employee_2 = Employee_()                     #'Employee_' class, hence they are Class Instances.
print(employee_1)                           #When you print these, you'll see they are called 'Employee_
print(employee_2)                           #objects', and are unique, with different memory addresses

#Lets give each of these employees some atttributes: First name, last name, email, and pay
employee_1.first = 'Corey'
employee_1.last = 'Schafer'
employee_1.email = 'Corey.Schafer@company.com'
employee_1.pay = 50000

employee_2.first = 'Test'
employee_2.last = 'User'
employee_2.email = 'Test.User@company.com'
employee_2.pay = 60000

#As you can see, this is a lot of work. Hence it will be great if we can add these attributes into the
#'Employee_' class so whenever we create an Employee_ object it will automatically have these attributes
#without typing them manually whenever you create an Employee_ object as seen above

#///////////////////////////////

#This '__init__' function is a Special Method (more on these in Tutorial 5) that describes the attributes
#(theres 4 in this example, '.first', '.last', '.pay' and '.email') of an object (it is not a normal 
#method but is still technically a method). You can think of it as initialiser/constructor.

#When you create a function in a Class (a method), it always takes in the Class Instance as the first
#parameter. By convention, we call this parameter 'self', even though it technically can be anything.

#Notice we did not add an email parameter as it can actually be created from the 'first' and 'last'
#parameters already.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first                                #By right, the 'first' in 'self.first' can be
        self.last = last                                  #anything ('fname' also can), just that you
        self.pay = pay                                    #will need to use that name whenever you want
        self.email = first + '.' + last +'@company.com'   #to see that attribute of the Class Instance
                                                          #made from this Class in the Terminal. Usually
                                                          #we'll keep it the same name as the parameter 
                                                          #in the method.

#Now, lets create a method (function in a Class) returning the full name of an employee.

#A very common error is where people forget to pass in the 'self' parameter here for the methods as in
#the main code when they call this method normally there is no need to pass any parameters in (just an
#empty curly brackets '()'), but the 'self' parameter is already technically called in in the main
#code's 'fullname' function when it is attached to the Class Instance in 'emp_1' in 'emp_1.fullname()'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)      #Can check how the '.format()' works in the
                                                          #documentation

#When you create the object, there is no need to have a 'self' parameter as the 'self' parameter
#takes the Class Instance which is already passed automatically when the Class Instance is made, hence, 
#you only need to call the other 3 parameters for your 'Employee' object (Class Instance) to be created.

#The order of 'Corey', 'Schafer' and '50000' matters btw so it corresponds to the 'first', 'last' and 
#'pay' variables in the 'Employee' Class
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1.email)                                        #This is how you called out an attribute from
print(emp_2.email)                                        #'Employee' object

#Without the fullname function it would be print('{} {}'.format(emp_1.first, emp_1.last)), but we
#already put this code up under the '.fullname()' method.
print(emp_1.fullname())

#Another way to represent this that better shows the inner workings of the method and the 'self'
#parameter is this. Here it shows the 'emp_1' being passed as the 'self' parameter in the 'fullname'
#method in the 'Employee' class. It does the exact thing as the line of code above.
print(Employee.fullname(emp_1))