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


class Developer(Employee):

    raised_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language     


#Creating the 'Manager' Subclass
class Manager(Employee):

    #Creates the attributes of a 'Manager' object. The additional attribute checks which are the Employees/
    #Developers they are in charge of supervising. This attribute is meant to accept a list of Employees/
    #Developers. If no list/inputs for this parameter (means the Manager is not supervising anyone), 
    #this attribute will be by default 'None', and return an empty list and nothing is shown in the output

    #Notice that the default value of 'employees' varaiable is set to be 'None' instead of an empty list
    #or dictionary. It is a rule in programming that you should not pass empty lists/dictionaries as 
    #default values as it may create unwanted behaviour when you run the code with lists and dictionaries
    #as default arguments. A way to solve this is by passing default value as 'None', and using an if
    #statement shown below.
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    #Creates a method to add an employee to the 'employees' list in the 'employees' Manager attribute
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    #Creates a method to remove an employee to the 'employees' list in the 'employees' Manager attribute
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    #Creates a method to print out the fullname of the 'employees' in the 'employees' list attribute
    #of a Manager.

    #Now you might think why can't I just put 'print(mgr_1.employees)' to get the names of the Employees?
    #This is because the 'employee' lists are filled with 'Employee' and 'Developer' objects, which you
    #cannot simply print out using print(emp_1) or print(dev_1). If you do 'print(mgr_1.employees)',
    #you telling Python to print a lists of such objects, which will give you not the name of the 
    #employees, but '[<__main__.Developer object at 0x000001F005E65590>]' instead.

    #Hence the need for this method to tell Python to use the '.fullname()' method to print out the
    #full name of each employee/developer in the list
    def print_emp(self):
        print('Manager', self.fullname(), '\nEmployees:')
        for i in self.employees:                         #More on how the 'isinstance()' function works
            if isinstance(i, Developer) == True:         #explained below    
                print('-->', i.fullname(), '(Developer)', '-', i.programming_language)
            elif isinstance(i, Developer) == False:
                print('-->', i.fullname(), '(Employee)')
        print('\n')

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Jane', 'Smith', 60000, 'Java')

mgr_1 = Manager('Sam', 'Doe', 90000, [dev_1])
mgr_2 = Manager('Sue', 'Smith', 80000, [emp_1, emp_2, dev_2])

print(mgr_1.email)

#This line shows why you can't just simply 'print(mgr_1.employees)' but need to create another whole
#method to print out the full name of each employee supervised by the Manager (explained on top at the
#'print_emp()' method)
print(mgr_1.employees)

mgr_1.print_emp()
mgr_2.print_emp()

#////////////////////////////////////////

#About the 'isinstance()' function.
#Takes in 'isinstance(object, classinfo)'. It is an inbuilt function into Python that allows you to 
#check if an object/variable's is an instance of a Class. It checks if the 'object' is of the class 
#provided into the 'classinfo' if it is it will return True, else False. (more functionality in 
#documentation)

#This will give an output True
x = 90
print(x, int)

#This will print True
print(isinstance(mgr_1, Manager))

#This will also print True, as 'Manager' is a SubClass/Inherited from the 'Employee' Class hence 'mgr_1' 
#gives True for the 'Employee' Class
print(isinstance(mgr_1, Employee))

#This will print False as even though 'Manager' and 'Developers' are SubClasses of the 'Employee' Class,
#it is not inherited by each other hence 'isinstance()' will return False.
print(isinstance(mgr_1, Developer))

#///////////////////////////////////

#About the 'issubclass()' function.
#Takes in 'issubclass(classinfo, classinfo)'. It is also an inbuilt function into Python that allows you 
#to check if the first provided 'classinfo' Class is a subclass of the second 'classinfo' Class.

#This will give an output True, as the 'Manager' Class is a subclass of 'Employee' Class
print(issubclass(Manager, Employee))

#This will give an output False, as the 'Manager' Class is not a subclass of 'Developer' Class
print(issubclass(Manager, Developer))

#This will give an output True. (fyi)
print(issubclass(Manager, Manager))