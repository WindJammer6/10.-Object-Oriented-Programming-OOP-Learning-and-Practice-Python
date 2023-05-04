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


#Lets say we want Developers to have a higher pay raise of 10% instead of the 4% of a regular Employee.
#We can do this by adding the Class variable 'raised_amount' into the SubClass, but assign it to 1.10 
#instead of 1.04 (Checking in main code)
class Developer(Employee):
    raised_amount = 1.10

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

dev_1 = Developer('John', 'Doe', 50000)
dev_2 = Developer('Jane', 'Smith', 60000)

#From here we can see that 'emp_1' and 'dev_1' both have the same pay, but after the 'apply_raise()'
#'dev_1' has a 10% raise while 'emp_1' still have the 4% raise

#The lesson to take away here is that we can make changes to our SubClasses, without affecting the 
#parent Class
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


