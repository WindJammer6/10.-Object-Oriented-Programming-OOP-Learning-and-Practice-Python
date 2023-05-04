class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#Lets say we made a change to the employee's first name to 'Jim' instead of 'Corey', notice when you 
#re-print 'emp_1' first, email and fullname, the first and fullname is updated to the change in first
#name to 'Jim', the email of emp_1 remains at 'Corey.Schafer@company.com' instead of 
#'Jim.Schafer@company.com' that we might have expected to happen.

#The reason why the 'fullname(self)' method works is because everytime its called it gets the current
#'first' and 'last' name of the employee, which will be, for the first name, currently 'Jim' (after the
#change) and not 'Corey'.

#The reason why the 'email' dosen't work is because once the object is created, the code in the '__init__'
#method is ran once to create the 'email' for 'emp_1' and when you change the first name of the 'Employee'
#object after the creation the code that creates the attributes under the '__init__' method is not run
#again to update the 'email' of the 'Employee' onject,  while only the update only updates the first
#name of the 'Employee' object and nothing else happens ('email' attribute is not updated)

#Now, your first thought to tackle this might be create a seperate email method (convert it from an
#attribute to a method). But the problem with this is that this will crash everyone's code who are using
#our 'Employee' Class and they will have to change all their 'email' in their code from attributes to a
#method (without the '()' (attributes) to with '()' (methods).

#To tackle this such as they don't have to add in the parenthesis and edit their code, is for us to make
#use of the Property Decorators - Getters and Setters
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())