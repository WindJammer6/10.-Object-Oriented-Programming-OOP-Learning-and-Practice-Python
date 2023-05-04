#What is the Getter Property Decorator?
#Implemented using '@property', it declares the method as a property (something like an attribute).
#Read the example below to see what kind of scenarios it is used.

#Property vs Attributes
#--> Attributes are defined by data variables like name, age, height etc. 
#--> Properties are special type of attributes. Property method comes with the getter, setter and delete
#    methods like __get__, __set__, and __delete__ methods. 

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    #This is how we implement a Getter Property Decorator. First, we implement an 'email' method like how
    #we might do to change the 'email' from an attribute to a method. (remember to remove the 'self.email'
    #attribute in the '__init__' method)

    #But this isn't what we want as other codes using our 'Employee' Class in the code will crash and will
    #have to change their code's 'email' to 'email()' instead

    #So how do we not crash other people's code who are using our 'Empolyee' object by letting 'email'
    #maintain as an attribute and not convert it into a method ('email()')? This is where adding the 
    #Getter Property Decorator will solve our problem. By adding the Getter Property Decorator, we can 
    #keep accessing our 'email' as an property/attribute instead of a method, while being able to update 
    #any changes in our 'Employee' object's first and last name into its 'email' attribute.

    @property                       #This is the Getter Property Decorator
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)  

    #We can add the Getter Property Decorator to our 'fullname(self)' method also to convert it to a
    #property/attribute. As you can see, once we add the Getter Property Decorator to our 'fullname(self)'
    #method, we can omit the '()' behind whenever we call the method in our main code.

    @property                       #This is the Getter Property Decorator
    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.first = 'Jim'

print(emp_1.first)

#Notice after adding the Getter Property Decorator to the 'email(self)' method (now is no longer a method,
#but a property/attribute after adding the Getter Property Decorator), this prints the correct output, 
#with the updated email after the first name of 'emp_1' is changed of 'Jim.Schafer@company.com' instead 
#of 'Corey.Schafer@company.com'
print(emp_1.email)

#Notice after adding Getter Property Decorator to the 'fullname(self)' method, it is now a property/
#attribute and there is no longer a need to have the '()' whenever you want to get the full name of an
#employee
print(emp_1.fullname)