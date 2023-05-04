#What is __add__?
#It returns a new object that represents the sum of two objects. As seen from 
#'1. Special_Methods_and_Operator_Overloading.py', it is an operator overloaded to be able to function
#differently in different contexts (ints, strings, lists). It is represented by the '+' operator.

#Lets customise it in our code so that it can take the sum of the pay of 2 employees as the result
#by adding the 2 'Employee' objects together. (This is not the best way to do this in real life
#as its better to be specific to exactly what you are doing in your functions but lets just do this 
#for the sake of the explanation)

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
    
    #In our '__add__(self, other)' Special Method we are assuming that this method is taking in 2 
    #'Employee' objects as its arguments
    def __add__(self, other):
        return self.pay + other.pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#These shows that the '__add__(self, other)' Special Method now works, and we can now 'add' 2 'Employee'
#objects together to get their total pay
print(emp_1 + emp_2)
print(Employee.__add__(emp_1, emp_2))