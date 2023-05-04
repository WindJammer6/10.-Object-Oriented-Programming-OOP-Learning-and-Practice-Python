#What are Alternate Constructors?
#Class Methods can also be used as Alternate Constructors. It means these Class Methods can provide
#alternate ways of creating your Class objects. (Can think of Alternate Constructors as a usage of
#Class Methods)

#In the example below, the default way of creating an 'Employee' object is:
#   emp_1 = Employee('Corey', 'Schafer', 50000)

#What if there is someone who wants to use our 'Employee' Class but are getting their employee information
#in the form of strings, that is seperated by hyphens, and they constantly need to parse (split) the
#manually into the respective 'first', 'last' and 'pay' of the employee. So we can create a Class
#method that can help them to automatically create the 'Employee' object by passing their hyphen-string
#employee info through it. Such a Class Method will be called an Alternate Constructor.

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

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

    #This is the Alternate Constructor (Class Method) for the person using our 'Employee' Class to easily
    #just pass thier employee info string into this function/method to immediately obtain an 'Employee'
    #object without manually splitting the string everytime they want to create an 'Employee' object

    #Note: The 'from' in 'from_string' is a convention naming used when creating a Alternate Constructor
    @classmethod
    def from_string(cls, hyphened_employee_info):
        first, last, pay = hyphened_employee_info.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#////////////////////////////

#These are examples of the incoming employee information. Without an Alternate Constructor (Class Method),
#the person using our 'Employee' Class has to manually split the strings via the code below, before
#passing the first, last and pay variables through our 'Employee' Class:
emp_str_10 = 'John-Doe-30000'
emp_str_11 = 'Jane-Smith-90000'
emp_str_12 = 'Sam-Doe-70000'

emp_str_10_first, emp_str_10_last, emp_str_10_pay = emp_str_10.split('-')
print(emp_str_10_first)

#As you could see the manual split coding of the string works. Now we will make use of the Alternate
#Constructor '.from_string()' method to make life easier for the perosn using our 'Employee' Class
test_new_emp_10 = Employee(emp_str_10_first, emp_str_10_last, emp_str_10_pay)
print(test_new_emp_10.email)
print(test_new_emp_10.pay)

#/////////////////////////////

#Here we use our Alternate Constructor, and checking if the object exists by printing out the employee's
#full name:
emp_3 = Employee.from_string(emp_str_11)
print(emp_3.fullname()) 



