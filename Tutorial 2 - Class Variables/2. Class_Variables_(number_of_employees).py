#We will now introduce another Class Variable (number_of_employees) which count the number of employees in
#the company by counting the number of 'Employee' objects created. How this works is that we do it by
#counter method, first setting the Class Variable 'number_of_employees' as 0, and since the '__init__'
#always run once whenever an 'Employee' object is created, we set this counter to be incremented whenever
#the '__init__' function is called

class Employee:

    number_of_employees = 0
    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        #Incremention of the 'number_of_employee' Class Variable by 1 whenever the '__init__' method
        #is called.

        #Notice we access this Class Variable through the Class (Employee) instead of the Class Instance 
        #(self) since its ok that it will be locked and not able to be changed from the main code by a 
        #specific Class Instance since we likely won't have to anyway as whenever an 'Employee' object
        #is created the counter must only go up by 1 (cannot be 2 or 3 since that is illogical)
        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

#Before declaring the 'Employee' objects the counter is 0
print(Employee.number_of_employees)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#After declaring the 'Employee' objects the counter is 2 (as the '__init__' method has been called twice)
print(Employee.number_of_employees)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
