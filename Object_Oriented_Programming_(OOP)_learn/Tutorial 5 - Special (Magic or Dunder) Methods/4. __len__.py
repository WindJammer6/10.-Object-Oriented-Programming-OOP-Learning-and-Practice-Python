#What is __len__?
#It returns the length of a string/list. 

#Lets customise it in our code so that it can find the number of characters of our employee's full name.

class Employee:

    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    #This is our '__len__(self)' Special Method. Returns length of the employee's full name (including
    #spacing)
    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#These shows that the '__len__(self, other)' Special Method now works, and we can now find the length of
#our 'Employee' objects (that is to give us the number of characters in their full name (including
#spacing))
print(len(emp_1))
print(emp_1.__len__())